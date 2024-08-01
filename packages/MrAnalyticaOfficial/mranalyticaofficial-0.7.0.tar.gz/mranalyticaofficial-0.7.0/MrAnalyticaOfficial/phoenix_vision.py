import cv2
import os
import numpy as np
import time
import random
import psutil
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

try:
    import tensorflow as tf
    from tensorflow.keras.models import Model
    from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
    from tensorflow.keras.applications import MobileNetV2
    from tensorflow.keras.optimizers import Adam
    from tensorflow.keras.callbacks import EarlyStopping
    TENSORFLOW_AVAILABLE = True
except ImportError:
    TENSORFLOW_AVAILABLE = False

class PhoenixVision:
    def __init__(self, fotos_dir):
        self.fotos_dir = fotos_dir
        self.rostos = []
        self.labels = []
        self.show_certainty = False
        self.show_stats = False
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.detection_mode = "face"
        self.camera_index = 0
        self.camera_url = None
        self.recognition_threshold = 0.5  # Valor padrão
        self.face_size_range = ((30, 30), (300, 300))  # Valor padrão
        self.model = None
        self.label_encoder = LabelEncoder()
        self.frame_count = 0
        self.start_time = time.time()
        self.total_faces_detected = 0
        self.img_size = (128, 128)  # Tamanho reduzido da imagem

    def _carregar_fotos(self):
        for pessoa in os.listdir(self.fotos_dir):
            pessoa_dir = os.path.join(self.fotos_dir, pessoa)
            if os.path.isdir(pessoa_dir):
                for imagem in os.listdir(pessoa_dir):
                    imagem_path = os.path.join(pessoa_dir, imagem)
                    img = cv2.imread(imagem_path)
                    if img is not None:
                        img = cv2.resize(img, self.img_size)
                        self.rostos.append(img)
                        self.labels.append(pessoa)

    def _preparar_dados(self):
        self._carregar_fotos()
        self.rostos = np.array(self.rostos) / 255.0  # Normalizar
        self.labels = self.label_encoder.fit_transform(self.labels)

    def _criar_modelo(self):
        base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(*self.img_size, 3))
        for layer in base_model.layers:
            layer.trainable = False

        x = GlobalAveragePooling2D()(base_model.output)
        x = Dense(512, activation='relu')(x)
        x = Dropout(0.3)(x)
        num_classes = len(set(self.labels))
        outputs = Dense(num_classes, activation='softmax')(x)

        self.model = Model(inputs=base_model.input, outputs=outputs)
        self.model.compile(optimizer=Adam(learning_rate=0.001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    def treinar(self):
        if not TENSORFLOW_AVAILABLE:
            print("TensorFlow não está instalado. Por favor, instale-o para usar esta funcionalidade.")
            return
        print("Preparando dados...")
        self._preparar_dados()
        if len(self.rostos) == 0:
            print("Nenhuma imagem encontrada no diretório de fotos. Verifique se o caminho está correto e se há imagens nas pastas.")
            return
        print("Criando modelo...")
        self._criar_modelo()
        print("Treinando modelo...")
        X_train, X_test, y_train, y_test = train_test_split(self.rostos, self.labels, test_size=0.2, random_state=42)
        
        early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
        
        self.model.fit(X_train, y_train, epochs=5, batch_size=64, 
                       validation_data=(X_test, y_test), callbacks=[early_stopping])
        print("Treinamento concluído!")

    def set_detection_mode(self, mode):
        valid_modes = ["face", "face_eyes"]
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

    def set_face_size_range(self, min_size, max_size):
        self.face_size_range = ((min_size, min_size), (max_size, max_size))
        print(f"Intervalo de tamanho de face definido para: {min_size} - {max_size}")

    def certainty(self, show=True):
        self.show_certainty = show

    def statsfornerds(self, show=True):
        self.show_stats = show

    def _detect_and_recognize(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=self.face_size_range[0], maxSize=self.face_size_range[1])
        
        for (x, y, w, h) in faces:
            face_roi = frame[y:y+h, x:x+w]
            face_roi = cv2.resize(face_roi, self.img_size)
            face_roi = np.expand_dims(face_roi, axis=0) / 255.0
            
            predictions = self.model.predict(face_roi, verbose=0)
            max_prob = np.max(predictions)
            if max_prob > self.recognition_threshold:
                person_id = np.argmax(predictions)
                person_name = self.label_encoder.inverse_transform([person_id])[0]
                label = f"{person_name} ({max_prob:.2f})" if self.show_certainty else person_name
                color = (0, 255, 0)
            else:
                label = "Desconhecido"
                color = (0, 0, 255)
            
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        return frame, len(faces)

    def start(self):
        if not TENSORFLOW_AVAILABLE:
            print("TensorFlow não está instalado. O reconhecimento facial avançado não estará disponível.")
            # Aqui você pode implementar uma versão mais simples de reconhecimento facial
            return
        if self.model is None:
            print("Modelo não treinado. Por favor, execute o método 'treinar()' primeiro.")
            return
        if self.model is None:
            print("Modelo não treinado. Por favor, execute o método 'treinar()' primeiro.")
            return

        if self.camera_url:
            video_capture = cv2.VideoCapture(self.camera_url)
        else:
            video_capture = cv2.VideoCapture(self.camera_index)

        while True:
            ret, frame = video_capture.read()
            if not ret:
                print("Falha ao capturar o frame. Verifique a conexão com a câmera.")
                break

            frame, num_faces = self._detect_and_recognize(frame)
            
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