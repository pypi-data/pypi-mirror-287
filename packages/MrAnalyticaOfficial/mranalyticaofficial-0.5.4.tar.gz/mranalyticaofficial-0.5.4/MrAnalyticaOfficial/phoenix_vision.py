import cv2
import mediapipe as mp
import os
import numpy as np
import face_recognition
from PIL import Image

class PhoenixVision:
    def __init__(self, certainty=True, stats_for_nerds=True, fotos_dir='fotos'):
        self.certainty = certainty
        self.stats_for_nerds = stats_for_nerds
        self.fotos_dir = fotos_dir
        self.mp_face_detection = mp.solutions.face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5)
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose.Pose()
        self.mp_face_mesh = mp.solutions.face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True)
        self.codificacoes_referencia = []
        self.nomes_referencia = []

    def carregar_imagens_referencia(self):
        for nome_pessoa in os.listdir(self.fotos_dir):
            pasta_pessoa = os.path.join(self.fotos_dir, nome_pessoa)
            if os.path.isdir(pasta_pessoa):
                for arquivo in os.listdir(pasta_pessoa):
                    caminho_imagem = os.path.join(pasta_pessoa, arquivo)
                    imagem = face_recognition.load_image_file(caminho_imagem)
                    codificacoes = face_recognition.face_encodings(imagem)
                    if codificacoes:
                        self.codificacoes_referencia.append(codificacoes[0])
                        self.nomes_referencia.append(nome_pessoa)

    def process_frame(self, frame):
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_results = self.mp_face_detection.process(image_rgb)
        pose_results = self.mp_pose.process(image_rgb)
        face_mesh_results = self.mp_face_mesh.process(image_rgb)

        if self.stats_for_nerds:
            if face_results.detections:
                for detection in face_results.detections:
                    self.mp_drawing.draw_detection(frame, detection)
                    if self.certainty:
                        bboxC = detection.location_data.relative_bounding_box
                        h, w, _ = frame.shape
                        cv2.putText(frame, f'{int(detection.score[0] * 100)}%',
                                    (int(bboxC.xmin * w), int(bboxC.ymin * h) - 10),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

            if pose_results.pose_landmarks:
                self.mp_drawing.draw_landmarks(frame, pose_results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)

            if face_mesh_results.multi_face_landmarks:
                for face_landmarks in face_mesh_results.multi_face_landmarks:
                    self.mp_drawing.draw_landmarks(
                        image=frame,
                        landmark_list=face_landmarks,
                        connections=mp.solutions.face_mesh.FACEMESH_TESSELATION,
                        landmark_drawing_spec=None,
                        connection_drawing_spec=mp.solutions.drawing_styles.get_default_face_mesh_tesselation_style()
                    )

        face_locations = face_recognition.face_locations(image_rgb)
        face_encodings = face_recognition.face_encodings(image_rgb, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(self.codificacoes_referencia, face_encoding)
            name = "Desconhecido"
            confidence = 0

            if True in matches:
                face_distances = face_recognition.face_distance(self.codificacoes_referencia, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = self.nomes_referencia[best_match_index]
                    confidence = 1 - face_distances[best_match_index]

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, f'{name} ({int(confidence * 100)}%)', (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

        return frame

    def start(self):
        self.carregar_imagens_referencia()
        cap = cv2.VideoCapture(0)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = self.process_frame(frame)
            cv2.imshow('PhoenixVision', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()