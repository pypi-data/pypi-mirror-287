import cv2
import os
import numpy as np
import face_recognition

class PhoenixVision:
    def __init__(self, fotos_dir):
        self.fotos_dir = fotos_dir
        self.known_face_encodings = []
        self.known_face_names = []
        self.show_certainty = False
        self.show_stats_for_nerds = False
        self._carregar_fotos()

    def _carregar_fotos(self):
        for nome_pessoa in os.listdir(self.fotos_dir):
            pessoa_dir = os.path.join(self.fotos_dir, nome_pessoa)
            for nome_imagem in os.listdir(pessoa_dir):
                imagem_path = os.path.join(pessoa_dir, nome_imagem)
                imagem = face_recognition.load_image_file(imagem_path)
                if len(face_recognition.face_encodings(imagem)) > 0:
                    encoding = face_recognition.face_encodings(imagem)[0]
                    self.known_face_encodings.append(encoding)
                    self.known_face_names.append(nome_pessoa)

    def certainty(self, show=True):
        self.show_certainty = show

    def statsfornerds(self, show=True):
        self.show_stats_for_nerds = show

    def start(self):
        video_capture = cv2.VideoCapture(0)

        while True:
            ret, frame = video_capture.read()
            rgb_frame = frame[:, :, ::-1]

            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                name = "Unknown"
                confidence = 0

                face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = self.known_face_names[best_match_index]
                    confidence = (1 - face_distances[best_match_index]) * 100

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                text = name
                if self.show_certainty:
                    text += f' ({confidence:.2f}%)'
                cv2.putText(frame, text, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                if self.show_stats_for_nerds:
                    landmarks = face_recognition.face_landmarks(rgb_frame, [(top, right, bottom, left)])[0]
                    for feature, points in landmarks.items():
                        for point in points:
                            cv2.circle(frame, point, 2, (255, 0, 0), -1)
                        for i in range(len(points) - 1):
                            cv2.line(frame, points[i], points[i + 1], (0, 255, 255), 1)

            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()
