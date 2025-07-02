from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QTimer, pyqtSignal, Qt
import cv2


class HomeView(QWidget):
    new_user_clicked = pyqtSignal()
    view_users_clicked = pyqtSignal()
    login_history_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setFixedSize(720, 1080)
        layout = QVBoxLayout(self)

        # Camera Feed
        self.camera_label = QLabel("Camera Feed")
        self.camera_label.setFixedSize(680, 680)
        self.camera_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.camera_label)

        # Buttons
        btn_layout = QVBoxLayout()
        self.new_user_btn = QPushButton("New User")
        self.options_btn = QPushButton("Options")
        self.new_user_btn.setFixedSize(680, 140)
        self.options_btn.setFixedSize(680, 140)

        self.new_user_btn.clicked.connect(self.new_user_clicked)
        self.options_btn.clicked.connect(self.view_users_clicked)  # for now
        btn_layout.addWidget(self.new_user_btn)
        btn_layout.addWidget(self.options_btn)
        layout.addLayout(btn_layout)

        # Camera
        self.cap = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_camera)

    def start_camera(self):
        self.cap = cv2.VideoCapture(0)
        self.timer.start(30)

    def stop_camera(self):
        self.timer.stop()
        if self.cap:
            self.cap.release()
            self.cap = None

    def update_camera(self):
        if self.cap:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.resize(frame, (720, 720))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = QImage(frame.data, frame.shape[1], frame.shape[0],
                             frame.strides[0], QImage.Format_RGB888)
                self.camera_label.setPixmap(QPixmap.fromImage(img))
