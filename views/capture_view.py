from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, Qt


from ui.style import apply_green_button_style , apply_red_button_style


class CaptureView(QWidget):
    capture_clicked = pyqtSignal()
    confirm_clicked = pyqtSignal()
    back_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setFixedSize(720, 1080)

        layout = QVBoxLayout(self)

        self.camera_label = QLabel("Camera feed will appear here")
        self.camera_label.setFixedSize(650, 650)
        self.camera_label.setAlignment(Qt.AlignCenter)
        self.image = QPixmap("assets/images/camera_placeholder.png")
        self.camera_label.setPixmap(self.image)
        layout.addWidget(self.camera_label)

        self.status_label = QLabel("Captured: 0 / 3")
        self.status_label.setFixedSize(650,50)
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)

        self.capture_button = QPushButton("Capture")
        self.capture_button.setFixedSize(650,70)
        self.capture_button.clicked.connect(self.capture_clicked.emit)
        layout.addWidget(self.capture_button)

        self.confirm_button = QPushButton("Confirm & Save")
        apply_green_button_style(self.confirm_button)
        self.confirm_button.setEnabled(False)
        self.confirm_button.setFixedSize(650,70)
        self.confirm_button.clicked.connect(self.confirm_clicked.emit)
        layout.addWidget(self.confirm_button)

        self.back_button = QPushButton("Back to Main")
        self.back_button.setFixedSize(650,70)
        self.back_button.clicked.connect(self.back_clicked.emit)
        layout.addWidget(self.back_button)

        layout.setContentsMargins(20,20,20,40)

    def update_capture_status(self, count):
        self.status_label.setText(f"Captured: {count} / 3")
        if count == 3:
            self.confirm_button.setEnabled(True)
            self.capture_button.setEnabled(False)

    def set_camera_frame(self, pixmap: QPixmap):
        self.camera_label.setPixmap(pixmap)
