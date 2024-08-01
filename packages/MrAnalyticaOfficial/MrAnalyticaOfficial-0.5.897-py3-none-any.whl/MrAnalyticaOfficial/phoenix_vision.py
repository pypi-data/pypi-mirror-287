import cv2
import os
import numpy as np
import time
import random
import psutil
import pickle
import dlib

class PhoenixVision:
    def __init__(self, fotos_dir):
        self.fotos_dir = fotos_dir
        self.rostos = []
        self.nomes = []
        self.show_certainty = False
        self.show_stats = False
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        self.detection_mode = "face"
        self.camera_index = 0
        self.camera_url = None
        self.recognition_threshold = 50  # Valor padrão
        self.face_size_range = (30, 300)  # Valor padrão
        self.enable_landmarks = False
        self.landmark_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
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

    def set_detection_mode(self, mode):
        valid_modes = ["face", "face_eyes", "face_full"]
        if mode not in valid_modes:
            raise ValueError(f"Modo inválido. Escolha entre: {', '.join(valid_modes)}")
        self.detection_mode = mode
        print(f"Modo de detecção alterado para: {mode}")

    def set_camera(self, camera_index_or_url):
        if isinstance(camera_index_or_url, int):
            self.camera_index = camera_index_or_url
            self.camera_url = None
        elif isinstance(camera_index_or_url, str):
            self.camera_url = camera_index_or_url
            self.camera_index = None
        else:
            raise ValueError("O argumento deve ser um índice de câmera (int) ou uma URL (str)")
        print(f"Câmera configurada para: {camera_index_or_url}")

    def set_recognition_threshold(self, threshold):
        self.recognition_threshold = threshold
        print(f"Limiar de reconhecimento definido para: {threshold}")

    def add_person(self, name, images):
        for image in images:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            self.rostos.append(gray)
            self.nomes.append(name)
        self._treinar()
        print(f"Pessoa {name} adicionada com {len(images)} imagens")

    def remove_person(self, name):
        indices = [i for i, n in enumerate(self.nomes) if n == name]
        for index in sorted(indices, reverse=True):
            del self.rostos[index]
            del self.nomes[index]
        self._treinar()
        print(f"Pessoa {name} removida")

    def save_model(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump((self.recognizer, self.nomes), f)
        print(f"Modelo salvo em {filename}")

    def load_model(self, filename):
        with open(filename, 'rb') as f:
            self.recognizer, self.nomes = pickle.load(f)
        print(f"Modelo carregado de {filename}")

    def set_face_size_range(self, min_size, max_size):
        self.face_size_range = (min_size, max_size)
        print(f"Intervalo de tamanho de face definido para: {min_size} - {max_size}")

    def enable_face_landmarks(self, enable):
        self.enable_landmarks = enable
        print(f"Detecção de pontos de referência facial {'ativada' if enable else 'desativada'}")

    def _draw_advanced_face_landmarks(self, frame, face):
        x, y, w, h = face
        center = (x + w // 2, y + h // 2)
        
        num_points = 30
        points = [(random.randint(x, x+w), random.randint(y, y+h)) for _ in range(num_points)]
        
        for point in points:
            cv2.circle(frame, point, 2, (0, 255, 255), -1)
        
        for i, point1 in enumerate(points):
            for point2 in points[i+1:]:
                distance = np.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
                if distance < w//3:
                    cv2.line(frame, point1, point2, (0, 255, 255), 1)
        
        cv2.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (0, 255, 255), 1)
        
        scan_height = int(self.frame_count % h)
        cv2.line(frame, (x, y + scan_height), (x + w, y + scan_height), (0, 255, 255), 1)

    def _detect_and_draw(self, frame, gray):
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=self.face_size_range[0], maxSize=self.face_size_range[1])
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            if self.detection_mode in ["face_eyes", "face_full"]:
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                eyes = self.eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)
            
            if self.enable_landmarks:
                shape = self.landmark_predictor(gray, dlib.rectangle(x, y, x+w, y+h))
                for i in range(68):
                    pt = (shape.part(i).x, shape.part(i).y)
                    cv2.circle(frame, pt, 2, (0, 255, 0), -1)
            
            face_roi = gray[y:y+h, x:x+w]
            id, confianca = self.recognizer.predict(face_roi)
            
            if confianca < self.recognition_threshold:
                nome = self.nomes[id]
                texto = nome
                if self.show_certainty:
                    texto += f' ({100 - int(confianca)}%)'
                cv2.putText(frame, texto, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            else:
                cv2.putText(frame, "Desconhecido", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            
            if self.show_stats:
                self._draw_advanced_face_landmarks(frame, (x, y, w, h))
        
        return frame, len(faces)

    def start(self):
        if self.camera_url:
            video_capture = cv2.VideoCapture(self.camera_url)
        else:
            video_capture = cv2.VideoCapture(self.camera_index)

        while True:
            ret, frame = video_capture.read()
            if not ret:
                print("Falha ao capturar o frame. Verifique a conexão com a câmera.")
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            frame, num_faces = self._detect_and_draw(frame, gray)
            
            self.frame_count += 1
            elapsed_time = time.time() - self.start_time
            fps = self.frame_count / elapsed_time
            self.total_faces_detected += num_faces

            if self.show_stats:
                stats_text = [
                    f"Modo de detecção: {self.detection_mode}",
                    f"FPS: {fps:.2f}",
                    f"Faces detectadas: {num_faces}",
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
        process = psutil.Process(os.getpid())
        return process.memory_info().rss / 1024 / 1024  # em MB