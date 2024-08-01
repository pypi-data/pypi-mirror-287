import cv2
import os
import numpy as np
import time
import random

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
        self.total_faces_detected = 0

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

    def _draw_advanced_face_landmarks(self, frame, face):
        x, y, w, h = face
        center = (x + w // 2, y + h // 2)
        
        # Gerar pontos aleatórios ao redor do rosto
        num_points = 30
        points = [(random.randint(x, x+w), random.randint(y, y+h)) for _ in range(num_points)]
        
        # Desenhar pontos
        for point in points:
            cv2.circle(frame, point, 2, (0, 255, 255), -1)
        
        # Desenhar linhas conectando pontos próximos
        for i, point1 in enumerate(points):
            for point2 in points[i+1:]:
                distance = np.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
                if distance < w//3:  # Ajuste este valor para mais ou menos conexões
                    cv2.line(frame, point1, point2, (0, 255, 255), 1)
        
        # Desenhar círculo ao redor do rosto
        cv2.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (0, 255, 255), 1)
        
        # Adicionar efeito de "escaneamento"
        scan_height = int(self.frame_count % h)
        cv2.line(frame, (x, y + scan_height), (x + w, y + scan_height), (0, 255, 255), 1)

    def start(self):
        video_capture = cv2.VideoCapture(0)
        while True:
            ret, frame = video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            
            self.frame_count += 1
            elapsed_time = time.time() - self.start_time
            fps = self.frame_count / elapsed_time
            self.total_faces_detected += len(faces)

            for (x, y, w, h) in faces:
                id, confianca = self.recognizer.predict(gray[y:y+h, x:x+w])
                nome = self.nomes[id]
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                texto = nome
                if self.show_certainty:
                    texto += f' ({100 - int(confianca)}%)'
                cv2.putText(frame, texto, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                
                if self.show_stats:
                    self._draw_advanced_face_landmarks(frame, (x, y, w, h))

            if self.show_stats:
                stats_text = [
                    f"FPS: {fps:.2f}",
                    f"Faces detectadas: {len(faces)}",
                    f"Total de faces detectadas: {self.total_faces_detected}",
                    f"Resolução: {frame.shape[1]}x{frame.shape[0]}",
                    f"Tempo decorrido: {elapsed_time:.2f}s",
                    f"Frames processados: {self.frame_count}",
                    f"Média de faces por frame: {self.total_faces_detected / self.frame_count:.2f}",
                    f"Uso de memória: {self._get_memory_usage():.2f} MB"
                ]
                for i, text in enumerate(stats_text):
                    cv2.putText(frame, text, (10, 30 + i*30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        video_capture.release()
        cv2.destroyAllWindows()

    def _get_memory_usage(self):
        import psutil
        process = psutil.Process(os.getpid())
        return process.memory_info().rss / 1024 / 1024  # em MB