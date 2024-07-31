import cv2
import mediapipe as mp
import os
import numpy as np
import face_recognition

class PhoenixVision:
    def __init__(self, certainty=False, stats_for_nerds=False, fotos_dir=None):
        self.certainty = certainty
        self.stats_for_nerds = stats_for_nerds
        self.fotos_dir = fotos_dir
        self.mp_face_detection = mp.solutions.face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5)
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose.Pose()
        self.imagens_referencia = {}
        self.codificacoes_referencia = []
        self.nomes_referencia = []
        self.face_results = None  # Novo atributo para armazenar os resultados da detecção de faces

    def process_frame(self, frame):
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.face_results = self.mp_face_detection.process(image_rgb) # Armazena os resultados em self.face_results
        pose_results = self.mp_pose.process(image_rgb)

        if self.stats_for_nerds:
            if self.face_results.detections:  # Usa self.face_results
                for detection in self.face_results.detections:
                    self.mp_drawing.draw_detection(frame, detection)
                    if self.certainty:
                        bboxC = detection.location_data.relative_bounding_box
                        h, w, _ = frame.shape
                        cv2.putText(frame, f'{int(detection.score[0] * 100)}%',
                                    (int(bboxC.xmin * w), int(bboxC.ymin * h) - 10),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

            if pose_results.pose_landmarks:
                self.mp_drawing.draw_landmarks(frame, pose_results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)

        return frame

    def set_certainty(self, enable=True):
        self.certainty = enable

    def set_stats_for_nerds(self, enable=True):
        self.stats_for_nerds = enable

    def start(self):
        cap = cv2.VideoCapture(0)

        for nome_pessoa in os.listdir(self.fotos_dir):
            pasta_pessoa = os.path.join(self.fotos_dir, nome_pessoa)
            if os.path.isdir(pasta_pessoa):
                for arquivo in os.listdir(pasta_pessoa):
                    imagem = face_recognition.load_image_file(os.path.join(pasta_pessoa, arquivo))
                    codificacao = face_recognition.face_encodings(imagem)[0]  
                    self.codificacoes_referencia.append(codificacao)
                    self.nomes_referencia.append(nome_pessoa)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = self.process_frame(frame)

            if self.face_results.detections: # Usa self.face_results
                for detection in self.face_results.detections:
                    bboxC = detection.location_data.relative_bounding_box
                    h, w, _ = frame.shape
                    x1, y1, x2, y2 = int(bboxC.xmin * w), int(bboxC.ymin * h), int((bboxC.xmin + bboxC.width) * w), int((bboxC.ymin + bboxC.height) * h)
                    rosto_detectado = frame[y1:y2, x1:x2]

                    codificacoes_rosto = face_recognition.face_encodings(rosto_detectado)
                    if codificacoes_rosto:
                        confiancas = face_recognition.face_distance(self.codificacoes_referencia, codificacoes_rosto[0])
                        indice_melhor_confianca = np.argmin(confiancas)
                        if confiancas[indice_melhor_confianca] < 0.6:
                            nome_pessoa = self.nomes_referencia[indice_melhor_confianca]
                            cv2.putText(frame, f'{nome_pessoa} ({int((1 - confiancas[indice_melhor_confianca]) * 100)}%)',
                                        (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

            cv2.imshow('PhoenixVision', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
