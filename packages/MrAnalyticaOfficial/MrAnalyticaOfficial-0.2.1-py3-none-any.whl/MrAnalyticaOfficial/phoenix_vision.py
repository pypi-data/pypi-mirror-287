import cv2
import os
import numpy as np

class PhoenixVision:
    def __init__(self, fotos_dir):
        self.fotos_dir = fotos_dir
        self.rostos = []
        self.nomes = []
        self.show_certainty = False
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self._carregar_fotos()
        self._treinar()

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

    def start(self):
        video_capture = cv2.VideoCapture(0)
        while True:
            ret, frame = video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            for (x, y, w, h) in faces:
                id, confianca = self.recognizer.predict(gray[y:y+h, x:x+w])
                nome = self.nomes[id]
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                texto = nome
                if self.show_certainty:
                    texto += f' ({100 - int(confianca)}%)'
                cv2.putText(frame, texto, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        video_capture.release()
        cv2.destroyAllWindows()
