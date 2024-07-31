import cv2
import mediapipe as mp

class PhoenixVision:
    def __init__(self, certainty=False, stats_for_nerds=False, fotos_dir=None):
        self.certainty = certainty
        self.stats_for_nerds = stats_for_nerds
        self.fotos_dir = fotos_dir 
        self.mp_face_detection = mp.solutions.face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5)
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose.Pose()

    def process_frame(self, frame):
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_results = self.mp_face_detection.process(image_rgb)
        pose_results = self.mp_pose.process(image_rgb)

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

        return frame

    def set_certainty(self, enable=True):
        self.certainty = enable

    def set_stats_for_nerds(self, enable=True):
        self.stats_for_nerds = enable

    def start(self):
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
