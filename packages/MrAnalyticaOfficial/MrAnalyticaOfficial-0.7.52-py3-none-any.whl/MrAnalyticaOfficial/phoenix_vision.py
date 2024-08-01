import cv2
import os
import numpy as np
import time
import psutil
import tensorflow as tf
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, BatchNormalization
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ReduceLROnPlateau, EarlyStopping, ModelCheckpoint
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from threading import Thread

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
        self.recognition_threshold = 0.7
        self.face_size_range = ((30, 30), (300, 300))
        self.model = None
        self.label_encoder = LabelEncoder()
        self.img_size = (224, 224)
        self.data_augmentation = ImageDataGenerator(
            rotation_range=20,
            width_shift_range=0.2,
            height_shift_range=0.2,
            horizontal_flip=True,
            zoom_range=0.2,
            brightness_range=[0.8, 1.2],
            preprocessing_function=self.preprocess_input
        )
        self.frame_count = 1
        self.start_time = time.time()
        self.total_faces_detected = 0
        self.stopped = False
        self.frame = None
        self.processed_frame = None

    def preprocess_input(self, img):
        return (img - 127.5) / 127.5

    def _carregar_fotos(self):
        for pessoa in os.listdir(self.fotos_dir):
            pessoa_dir = os.path.join(self.fotos_dir, pessoa)
            if os.path.isdir(pessoa_dir):
                for imagem in os.listdir(pessoa_dir):
                    imagem_path = os.path.join(pessoa_dir, imagem)
                    img = cv2.imread(imagem_path)
                    if img is not None:
                        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        img = cv2.resize(img, self.img_size)
                        self.rostos.append(img)
                        self.labels.append(pessoa)
        print(f"Total de imagens carregadas: {len(self.rostos)}")
        print(f"Distribuição de classes: {dict(zip(*np.unique(self.labels, return_counts=True)))}")

    def _preparar_dados(self):
        self._carregar_fotos()
        self.rostos = np.array(self.rostos)
        self.labels = self.label_encoder.fit_transform(self.labels)

    def _criar_modelo(self):
        base_model = EfficientNetB0(weights='imagenet', include_top=False, input_shape=(*self.img_size, 3))
        
        for layer in base_model.layers:
            layer.trainable = False

        x = base_model.output
        x = GlobalAveragePooling2D()(x)
        x = Dense(512, activation='relu')(x)
        x = BatchNormalization()(x)
        x = Dropout(0.5)(x)
        x = Dense(256, activation='relu')(x)
        x = BatchNormalization()(x)
        x = Dropout(0.5)(x)
        num_classes = len(set(self.labels))
        outputs = Dense(num_classes, activation='softmax')(x)

        self.model = Model(inputs=base_model.input, outputs=outputs)
        self.model.compile(optimizer=Adam(learning_rate=0.001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    def treinar(self):
        self._preparar_dados()
        self._criar_modelo()

        X_train, X_test, y_train, y_test = train_test_split(self.rostos, self.labels, test_size=0.2, stratify=self.labels, random_state=42)

        reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=5, min_lr=1e-6)
        early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
        model_checkpoint = ModelCheckpoint('best_model.h5', save_best_only=True, monitor='val_accuracy')

        history = self.model.fit(
            self.data_augmentation.flow(X_train, y_train, batch_size=32),
            epochs=100,
            validation_data=(X_test, y_test),
            callbacks=[reduce_lr, early_stopping, model_checkpoint]
        )

        # Fine-tuning
        for layer in self.model.layers[-20:]:
            layer.trainable = True

        self.model.compile(optimizer=Adam(learning_rate=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

        history_fine = self.model.fit(
            self.data_augmentation.flow(X_train, y_train, batch_size=32),
            epochs=50,
            validation_data=(X_test, y_test),
            callbacks=[reduce_lr, early_stopping, model_checkpoint]
        )

        # Evaluate the model
        test_loss, test_accuracy = self.model.evaluate(X_test, y_test)
        print(f"Acurácia final do modelo: {test_accuracy*100:.2f}%")

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
        print(f"Limiar de reconhecimento definido para: {threshold:.2f} ({threshold*100:.1f}%)")

    def set_face_size_range(self, min_size, max_size):
        self.face_size_range = ((min_size, min_size), (max_size, max_size))
        print(f"Intervalo de tamanho de face definido para: {min_size} - {max_size}")

    def certainty(self, show=True):
        self.show_certainty = show

    def statsfornerds(self, show=True):
        self.show_stats = show

    def _detect_and_recognize(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, 
                                                   minSize=(int(self.face_size_range[0][0]*0.5), int(self.face_size_range[0][1]*0.5)), 
                                                   maxSize=(int(self.face_size_range[1][0]*0.5), int(self.face_size_range[1][1]*0.5)))
        
        detected_faces = []
        for (x, y, w, h) in faces:
            face_roi = small_frame[y:y+h, x:x+w]
            face_roi = cv2.cvtColor(face_roi, cv2.COLOR_BGR2RGB)
            face_roi = cv2.resize(face_roi, self.img_size)
            face_roi = self.preprocess_input(face_roi)
            face_roi = np.expand_dims(face_roi, axis=0)
            
            predictions = self.model.predict(face_roi, verbose=0)
            max_prob = np.max(predictions)
            if max_prob > self.recognition_threshold:
                person_id = np.argmax(predictions)
                person_name = self.label_encoder.inverse_transform([person_id])[0]
                certainty_percentage = max_prob * 100
                label = f"{person_name} ({certainty_percentage:.1f}%)" if self.show_certainty else person_name
                color = (0, 255, 0)
            else:
                label = "Desconhecido"
                color = (0, 0, 255)
            
            detected_faces.append((x*2, y*2, w*2, h*2, label, color))

        for (x, y, w, h, label, color) in detected_faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        return frame, len(detected_faces)

    def _process_frame(self):
        while not self.stopped:
            if self.frame is not None:
                self.processed_frame, num_faces = self._detect_and_recognize(self.frame.copy())
                self.total_faces_detected += num_faces
                self.frame_count += 1
            else:
                time.sleep(0.01)

    def start(self):
        if self.model is None:
            print("Modelo não treinado. Por favor, execute o método 'treinar()' primeiro.")
            return

        if self.camera_url:
            video_capture = cv2.VideoCapture(self.camera_url)
        else:
            video_capture = cv2.VideoCapture(self.camera_index)

        self.stopped = False
        processing_thread = Thread(target=self._process_frame, args=())
        processing_thread.start()

        try:
            while True:
                ret, self.frame = video_capture.read()
                if not ret:
                    print("Falha ao capturar o frame. Verifique a conexão com a câmera.")
                    break

                frame_to_show = self.processed_frame if self.processed_frame is not None else self.frame

                elapsed_time = max(time.time() - self.start_time, 1)
                fps = self.frame_count / elapsed_time

                if self.show_stats:
                    stats_text = [
                        f"Modo de detecção: {self.detection_mode}",
                        f"FPS: {fps:.2f}",
                        f"Total de faces detectadas: {self.total_faces_detected}",
                        f"Resolução: {frame_to_show.shape[1]}x{frame_to_show.shape[0]}",
                        f"Tempo decorrido: {elapsed_time:.2f}s",
                        f"Frames processados: {self.frame_count}",
                        f"Média de faces por frame: {self.total_faces_detected / self.frame_count:.2f}",
                        f"Uso de memória: {self._get_memory_usage():.2f} MB"
                    ]
                    for i, text in enumerate(stats_text):
                        cv2.putText(frame_to_show, text, (10, 30 + i*30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

                cv2.imshow('Video', frame_to_show)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        finally:
            self.stopped = True
            processing_thread.join()
            video_capture.release()
            cv2.destroyAllWindows()

    def _get_memory_usage(self):
        process = psutil.Process(os.getpid())
        return process.memory_info().rss / 1024 / 1024  # em MB