from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage, QMovie
from PyQt5.QtCore import QTimer, pyqtSignal, Qt


class SuccessView(QWidget):
    home_btn_clicked = pyqtSignal()

    def __init__(self, data):
        super().__init__()
        self.setFixedSize(720, 1080)
        layout = QVBoxLayout(self)

        self.success_image = QLabel()
        self.success_image.setFixedSize(680,500)
        self.success_image.setAlignment(Qt.AlignCenter)

        self.movie = QMovie("assets/gifs/7efs.gif")
        self.success_image.setMovie(self.movie)

        self.movie.start()
        
        self.success_image.show()

        layout.addWidget(self.success_image)
        
        self.display_data = QLabel(data + ' Successfully')
        self.display_data.setFixedSize(680,50)
        self.display_data.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.display_data)


        self.home_btn = QPushButton("Back to Main")
        self.home_btn.setFixedSize(680, 140)
        self.home_btn.clicked.connect(self.home_btn_clicked.emit)

        layout.addWidget(self.home_btn)


    # def data_display(self, data):
    #     display_string = data
    #     print(display_string)
