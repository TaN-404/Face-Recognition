from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, 
                            QLabel, QLineEdit, QPushButton, QMessageBox)
from PyQt5.QtCore import Qt, pyqtSignal

from ui.style import apply_green_button_style , apply_red_button_style

class EditUserView(QWidget):
    save_clicked = pyqtSignal(dict)  # {uid, fname, lname}
    back_clicked = pyqtSignal()
    
    def __init__(self, user_data):
        super().__init__()
        self.setFixedSize(720, 1080)
        layout = QVBoxLayout(self)
        
        # UID (read-only)
        uid_layout = QHBoxLayout()
        uid_layout.addWidget(QLabel("UID:"))
        self.uid_field = QLineEdit()
        self.uid_field.setText(user_data['uid'])
        self.uid_field.setReadOnly(True)
        uid_layout.addWidget(self.uid_field)
        layout.addLayout(uid_layout)
        
        # First Name
        fname_layout = QHBoxLayout()
        fname_layout.addWidget(QLabel("First Name:"))
        self.fname_field = QLineEdit()
        self.fname_field.setText(user_data['fname'])
        fname_layout.addWidget(self.fname_field)
        layout.addLayout(fname_layout)
        
        # Last Name
        lname_layout = QHBoxLayout()
        lname_layout.addWidget(QLabel("Last Name:"))
        self.lname_field = QLineEdit()
        self.lname_field.setText(user_data['lname'])
        lname_layout.addWidget(self.lname_field)
        layout.addLayout(lname_layout)
        
        # Buttons
        btn_layout = QHBoxLayout()
        save_btn = QPushButton("Save Changes")
        apply_green_button_style(save_btn)
        save_btn.clicked.connect(self.handle_save)
        back_btn = QPushButton("Cancel")
        apply_red_button_style(back_btn)
        back_btn.clicked.connect(self.back_clicked.emit)
        
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(back_btn)
        layout.addLayout(btn_layout)
    
    def handle_save(self):
        """Collect data and emit save signal"""
        user_data = {
            'uid': self.uid_field.text(),
            'fname': self.fname_field.text(),
            'lname': self.lname_field.text()
        }
        self.save_clicked.emit(user_data)

    def show_message(self, title, message):
        """Show information message"""
        QMessageBox.information(self, title, message)