from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtCore import pyqtSignal


class NewUserView(QWidget):
    proceed_clicked = pyqtSignal(dict)
    back_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setFixedSize(720, 1080)

        layout = QVBoxLayout(self)

        self.title = QLabel("Register New User")
        self.title.setFixedSize(680,50)
        layout.addWidget(self.title)

        self.fname_input = QLineEdit()
        self.fname_input.setPlaceholderText("First Name")
        self.fname_input.setFixedSize(680,50)
        layout.addWidget(self.fname_input)

        self.lname_input = QLineEdit()
        self.lname_input.setPlaceholderText("Last Name")
        self.lname_input.setFixedSize(680,50)
        layout.addWidget(self.lname_input)

        self.uid_input = QLineEdit()
        self.uid_input.setPlaceholderText("User ID")
        self.uid_input.setFixedSize(680,50)
        layout.addWidget(self.uid_input)

        # Proceed button
        self.proceed_btn = QPushButton("Proceed")
        self.proceed_btn.clicked.connect(self.on_proceed)
        self.proceed_btn.setFixedSize(680,160)
        layout.addWidget(self.proceed_btn)

        # Back button
        self.back_btn = QPushButton("Back to Main")
        self.back_btn.clicked.connect(lambda: self.back_clicked.emit())
        self.back_btn.setFixedSize(680,160)
        layout.addWidget(self.back_btn)

    def on_proceed(self):
        user_data = {
            "fname": self.fname_input.text().strip(),
            "lname": self.lname_input.text().strip(),
            "uid": self.uid_input.text().strip()
        }
        self.proceed_clicked.emit(user_data)

    def clear_fields(self):
        self.fname_input.clear()
        self.lname_input.clear()
        self.uid_input.clear()
