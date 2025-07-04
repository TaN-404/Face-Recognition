from PyQt5.QtWidgets import (QTableView, QVBoxLayout, QWidget, 
                            QHeaderView, QPushButton,QMessageBox)
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, pyqtSignal


from ui.style import apply_green_button_style , apply_red_button_style

class LoginHistoryView(QWidget):
    home_btn_clicked = pyqtSignal()
    back_btn_clicked = pyqtSignal()
    clear_history_clicked = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setFixedSize(720, 1080)
        layout = QVBoxLayout(self)

        # Table View
        self.table_view = QTableView()
        self.table_view.setSortingEnabled(True)
        self.table_view.setFixedSize(650, 800)
        layout.addWidget(self.table_view)

        self.clear_history_btn = QPushButton("Clear History")
        self.clear_history_btn.setFixedSize(650,60)
        apply_red_button_style(self.clear_history_btn)
        self.clear_history_btn.clicked.connect(self.clear_history_clicked.emit)
        layout.addWidget(self.clear_history_btn)

        self.back_btn = QPushButton("Back")
        self.back_btn.setFixedSize(650,60)
        self.back_btn.clicked.connect(self.back_btn_clicked.emit)
        layout.addWidget(self.back_btn)

        # Home Button
        self.home_btn = QPushButton("Back to Main")
        self.home_btn.setFixedSize(650, 60)
        self.home_btn.clicked.connect(self.home_btn_clicked.emit)
        layout.addWidget(self.home_btn)
        layout.setContentsMargins(20,20,20,40)
        # Initialize empty model
        self.init_empty_model()

    def init_empty_model(self):
        """Initialize an empty table model"""
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels([
            "User ID", 
            "First Name", 
            "Last Name", 
            "Date", 
            "Time"
        ])
        self.table_view.setModel(model)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table_view.horizontalHeader().setStretchLastSection(True)

    def display_data(self, entries):
        """Display data in the table view"""
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels([
            "User ID", 
            "First Name", 
            "Last Name", 
            "Date", 
            "Time"
        ])
            
        for row in entries:
            # Create items and set them as non-editable
            uid_item = QStandardItem(str(row[0]))
            uid_item.setEditable(False)
            
            fname_item = QStandardItem(row[1])
            fname_item.setEditable(False)
            
            lname_item = QStandardItem(row[2])
            lname_item.setEditable(False)
            
            date_item = QStandardItem(row[3])
            date_item.setEditable(False)
            
            time_item = QStandardItem(row[4])
            time_item.setEditable(False)
            
            model.appendRow([
                uid_item,
                fname_item,
                lname_item,
                date_item,
                time_item
            ])

        self.table_view.setModel(model)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table_view.horizontalHeader().setStretchLastSection(True)

    def confirm_action(parent=None):
        reply = QMessageBox.question(
            parent,
            "Confirm",
            "Are you sure you want to proceed?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            print("User confirmed.")
            return True
        else:
            print("User cancelled.")
            return False