import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
import os

from models.user_model import UserModel

class OptionPresenter:
    def __init__(self, view, navigator):
        self.view = view
        self.navigator = navigator
        self.user_model = UserModel()

        self.view.back_button_clicked.connect(self.go_to_home)
        self.view.login_history_clicked.connect(self.go_to_login_history)
        self.view.user_list_clicked.connect(self.go_to_user_list)
        self.view.user_management_clicked.connect(self.go_to_user_management)


    def go_to_home(self):
        print("back button pressed")
        self.navigator("home")

    def go_to_login_history(self):
         self.navigator("login_history")
    
    def go_to_user_list(self):
        print("user list clicked")
        self.navigator("users_list")


    def go_to_user_management(self):
        self.navigator("user_management")