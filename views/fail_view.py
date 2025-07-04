from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage, QMovie
from PyQt5.QtCore import QTimer, pyqtSignal, Qt


class FailView(QWidget):
    home_btn_clicked = pyqtSignal()

    def __init__(self, data):
        super().__init__()
        self.setFixedSize(720, 1080)
        layout = QVBoxLayout(self)

        self.fail_image = QLabel()
        self.fail_image.setFixedSize(650,500)
        self.fail_image.setAlignment(Qt.AlignCenter)

        self.image = QPixmap("assets/images/fail.png")
        self.fail_image.setPixmap(self.image)

        layout.addWidget(self.fail_image)
        
        self.display_data = QLabel(data)
        self.display_data.setFixedSize(650,50)
        self.display_data.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.display_data)


        self.home_btn = QPushButton("Back to Main")
        self.home_btn.setFixedSize(650, 140)
        self.home_btn.clicked.connect(self.home_btn_clicked.emit)

        layout.addWidget(self.home_btn)
        layout.setContentsMargins(20,20,20,40)


    # def data_display(self, data):
    #     display_string = data
    #     print(display_string)
