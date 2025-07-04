from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, Qt


class OptionView(QWidget):
    login_history_clicked = pyqtSignal()
    user_list_clicked = pyqtSignal()
    user_management_clicked = pyqtSignal()
    back_button_clicked = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setFixedSize(720, 1080)

        layout = QVBoxLayout(self)

        self.login_history_btn = QPushButton("Login History")
        self.login_history_btn.setFixedSize(680,70)
        self.login_history_btn.clicked.connect(self.login_history_clicked.emit)
        layout.addWidget(self.login_history_btn)

        self.user_list_btn = QPushButton("User List")
        self.user_list_btn.setFixedSize(680,70)
        self.user_list_btn.clicked.connect(self.user_list_clicked.emit)
        layout.addWidget(self.user_list_btn)

        self.user_management_btn = QPushButton("User Management")
        self.user_management_btn.setFixedSize(680,70)
        self.user_management_btn.clicked.connect(self.user_management_clicked.emit)
        layout.addWidget(self.user_management_btn)

        self.back_button = QPushButton("Back to Main")
        self.back_button.setFixedSize(680,70)
        self.back_button.clicked.connect(self.back_button_clicked.emit)
        layout.addWidget(self.back_button)

