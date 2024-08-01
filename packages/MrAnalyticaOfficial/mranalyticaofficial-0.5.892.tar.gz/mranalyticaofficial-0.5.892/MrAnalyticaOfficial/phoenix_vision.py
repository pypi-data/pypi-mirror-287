import cv2
import os
import numpy as np
import time

class PhoenixVision:
    def __init__(self, fotos_dir):
        self.fotos_dir = fotos_dir
        self.rostos = []
        self.nomes = []
        self.show_certainty = False
        self.show_stats = False
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self._carregar_fotos()
        self._treinar()
        self.frame_count = 0
        self.start_time = time.time()

    def _carregar_fotos(self):
        for nome_pessoa in os.listdir(self.fotos_dir):
            for nome_imagem in os.listdir(os.path.join(self.fotos_dir, nome_pessoa)):
                imagem_path = os.path.join(self.fotos_dir, nome_pessoa, nome_imagem)
                imagem = cv2.imread(imagem_path)
                gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
                self.rostos.append(gray)
                self.nomes.append(nome_pessoa)

    def _treinar(self):
        self.recognizer.train(self.rostos, np.array(range(len(self.nomes))))

    def certainty(self, show=True):
        self.show_certainty = show

    def statsfornerds(self, show=True):
        self.show_stats = show

    def _draw_face_landmarks(self, frame, face):
        x, y, w, h = face
        landmarks = [
            (x + int(0.3 * w), y + int(0.3 * h)),
            (x + int(0.7 * w), y + int(0.3 * h)),
            (x + int(0.5 * w), y + int(0.6 * h)),
            (x + int(0.3 * w), y + int(0.8 * h)),
            (x + int(0.7 * w), y + int(0.8 * h))
        ]
        
        for point in landmarks:
            cv2.circle(frame, point, 2, (0, 255, 255), -1)
        
        for i in range(len(landmarks)):
            for j in range(i+1, len(landmarks)):
                cv2.line(frame, landmarks[i], landmarks[j], (0, 255, 255), 1)

    def start(self):
        video_capture = cv2.VideoCapture(0)
        while True:
            ret, frame = video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            
            self.frame_count += 1
            elapsed_time = time.time() - self.start_time
            fps = self.frame_count / elapsed_time

            for (x, y, w, h) in faces:
                id, confianca = self.recognizer.predict(gray[y:y+h, x:x+w])
                nome = self.nomes[id]
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                texto = nome
                if self.show_certainty:
                    texto += f' ({100 - int(confianca)}%)'
                cv2.putText(frame, texto, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                
                if self.show_stats:
                    self._draw_face_landmarks(frame, (x, y, w, h))

            if self.show_stats:
                stats_text = [
                    f"FPS: {fps:.2f}",
                    f"Faces detectadas: {len(faces)}",
                    f"Resolução: {frame.shape[1]}x{frame.shape[0]}",
                    f"Tempo decorrido: {elapsed_time:.2f}s"
                ]
                for i, text in enumerate(stats_text):
                    cv2.putText(frame, text, (10, 30 + i*30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        video_capture.release()
        cv2.destroyAllWindows()