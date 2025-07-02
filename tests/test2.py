import sys
import cv2
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, Qt


class CameraApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Camera App")
        self.setFixedSize(720, 1080)

        # --- Layouts ---
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # --- Camera Feed ---
        self.camera_label = QLabel(self)
        self.camera_label.setFixedSize(720, 720)
        self.camera_label.setStyleSheet("background-color: black;")
        self.camera_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.camera_label)

        # --- Button Row ---
        button_layout = QHBoxLayout()

        self.login_button = QPushButton("Login")
        self.login_button.setFixedSize(360, 360)
        button_layout.addWidget(self.login_button)

        self.register_button = QPushButton("Register")
        self.register_button.setFixedSize(360, 360)
        button_layout.addWidget(self.register_button)

        main_layout.addLayout(button_layout)

        # --- OpenCV Camera ---
        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # Resize and convert to RGB
            frame = cv2.resize(frame, (720, 720))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convert to QImage and display
            image = QImage(frame.data, frame.shape[1], frame.shape[0],
                           frame.strides[0], QImage.Format_RGB888)
            self.camera_label.setPixmap(QPixmap.fromImage(image))

    def closeEvent(self, event):
        self.cap.release()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CameraApp()
    window.show()
    sys.exit(app.exec_())
