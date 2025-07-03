import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
import os


class SuccessPresenter:
    def __init__(self, view, navigator, data):
        self.view = view
        self.navigator = navigator
        self.data = data

        self.view.home_btn_clicked.connect(self.go_to_home)
        self.view.__init__(self.data)


    def go_to_home(self):
            print("back button pressed")
            self.navigator("home")