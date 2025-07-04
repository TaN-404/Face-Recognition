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
        self.view.clear_db_clicked.connect(self.clear_db)


    def go_to_home(self):
        print("back button pressed")
        self.navigator("home")

    def go_to_login_history(self):
         self.navigator("login_history")
    
    def go_to_user_list(self):
        print("user list clicked")
        self.navigator("users_list")
    
    def clear_db(self):
        if self.view.confirm_action():
            self.user_model.drop_user_table()