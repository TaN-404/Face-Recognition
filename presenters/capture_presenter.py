import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
import os
from models.user_model import UserModel
import numpy as np


"""MODEL"""
from core.embed import embed_image



class CapturePresenter:
    def __init__(self, view, navigator, user_data):
        self.view = view
        self.navigator = navigator
        self.user_data = user_data
        self.captures = []
        self.embeddings = []

        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_camera_frame)
        self.timer.start(30)
        

        self.view.capture_clicked.connect(self.capture_face)
        self.view.confirm_clicked.connect(self.save_user)
        self.view.back_clicked.connect(self.exit_to_main)

    def update_camera_frame(self):
        ret, frame = self.cap.read()
        if ret:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_frame.shape
            bytes_per_line = ch * w
            qt_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qt_image).scaled(720, 720)
            self.view.set_camera_frame(pixmap)
            self.current_frame = frame

    def capture_face(self):
        embeded_image = embed_image(self.current_frame)

        self.captures.append(self.current_frame.copy())
        self.embeddings.append(embeded_image)

        self.view.update_capture_status(len(self.captures))

    def save_user(self):
        uid = self.user_data["uid"]
        image_dir = os.path.join("data", "images", uid)
        os.makedirs(image_dir, exist_ok=True)

        image_paths = []
        for i, img in enumerate(self.captures):
            path = os.path.join(image_dir, f"img{i+1}.jpg")
            cv2.imwrite(path, img)
            image_paths.append(path)

        avg_embedding = np.mean(self.embeddings, axis=0)

        user_model = UserModel()
        user_model.save_user(
            uid=uid,
            fname=self.user_data["fname"],
            lname=self.user_data["lname"],
            image_paths=image_paths,
            embeddings=self.embeddings,
            avg_embedding=avg_embedding
        )

        print("✅ User saved successfully!")
        self.exit_to_main()

    def exit_to_main(self):
        self.timer.stop()
        self.cap.release()
        self.navigator("home")
