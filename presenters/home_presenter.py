import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
import os
from models.user_model import UserModel
from core.embed import embed_image
from core.compare import compare_faces
import numpy as np

class HomePresenter:
    def __init__(self, view, navigator):
        self.view = view
        self.navigator = navigator  # function to change screens

        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_camera_frame)
        self.timer.start(30)
        
        
        self.view.login_btn_clicked.connect(self.login_function)
        self.view.new_user_clicked.connect(self.go_to_new_user)
        self.view.option_btn_clicked.connect(self.go_to_options)  # for now


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
    
    def login_function(self):
        user_model = UserModel()
        embedding = embed_image(self.current_frame)
        embedding_avg = user_model.get_all_avg_embeddings()
        # compare_faces(embedding, embedding_avg)

        is_match, similarity, average_e = compare_faces(embedding, embedding_avg)
        print(is_match)
        print(similarity)

        fullname = user_model.get_username_from_embedding(average_e)

        data = f"{fullname} Logged in"

        self.navigator("success", data)


    def go_to_new_user(self):
        self.stop_camera()
        self.navigator("new_user")

    def go_to_options(self):
        self.stop_camera()
        self.navigator("option") 
    
    def stop_camera(self):
        self.timer.stop()
        if self.cap:
            self.cap.release()
            self.cap = None

    def start_camera(self):
        self.cap = cv2.VideoCapture(0)
        self.timer.start(30)
