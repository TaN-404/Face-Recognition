import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
import os


class OptionPresenter:
    def __init__(self, view, navigator):
        self.view = view
        self.navigator = navigator

        self.view.back_button_clicked.connect(self.go_to_home)


    def go_to_home(self):
            print("back button pressed")
            self.navigator("home")