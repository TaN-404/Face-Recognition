from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout, QMessageBox
from PyQt5.QtCore import pyqtSignal, Qt


from ui.style import apply_green_button_style , apply_red_button_style

class NewUserView(QWidget):
    proceed_clicked = pyqtSignal(dict)
    back_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setFixedSize(720, 1080)

        layout = QVBoxLayout(self)
        btn_layout = QVBoxLayout()

        self.title = QLabel("Register New User")
        self.title.setFixedSize(650,50)
        self.title.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title)

        self.fname_input = QLineEdit()
        self.fname_input.setPlaceholderText("First Name")
        self.fname_input.setFixedSize(650,50)
        layout.addWidget(self.fname_input)

        self.lname_input = QLineEdit()
        self.lname_input.setPlaceholderText("Last Name")
        self.lname_input.setFixedSize(650,50)
        layout.addWidget(self.lname_input)

        self.uid_input = QLineEdit()
        self.uid_input.setPlaceholderText("User ID")
        self.uid_input.setFixedSize(650,50)
        layout.addWidget(self.uid_input)

        btn_layout.addStretch()
        # Proceed button
        self.proceed_btn = QPushButton("Proceed")
        self.proceed_btn.clicked.connect(self.on_proceed)
        apply_green_button_style(self.proceed_btn)
        self.proceed_btn.setFixedSize(650,160)
        btn_layout.addWidget(self.proceed_btn)

        # Back button
        self.back_btn = QPushButton("Back to Main")
        self.back_btn.clicked.connect(lambda: self.back_clicked.emit())
        self.back_btn.setFixedSize(650,160)
        btn_layout.addWidget(self.back_btn)
        # btn_layout.setContentsMargins(20,20,20,20)

        layout.addLayout(btn_layout)
        layout.setContentsMargins(20,20,20,40)

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

    def warning(self, message):
        QMessageBox.warning(self, "Warning", message)

