from PyQt5.QtWidgets import (QTableView, QVBoxLayout, QWidget, 
                            QHeaderView, QPushButton)
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, pyqtSignal

class LoginHistoryView(QWidget):
    home_btn_clicked = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setFixedSize(720, 1080)
        layout = QVBoxLayout(self)

        # Table View
        self.table_view = QTableView()
        self.table_view.setSortingEnabled(True)
        self.table_view.setFixedSize(680, 940)
        layout.addWidget(self.table_view)

        # Home Button
        self.home_btn = QPushButton("Back to Main")
        self.home_btn.setFixedSize(680, 90)
        self.home_btn.clicked.connect(self.home_btn_clicked.emit)
        layout.addWidget(self.home_btn)

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
            items = [
                QStandardItem(str(row[0])),  # UID
                QStandardItem(row[1]),       # First Name
                QStandardItem(row[2]),       # Last Name
                QStandardItem(row[3]),       # Date
                QStandardItem(row[4])        # Time
            ]
            model.appendRow(items)

        self.table_view.setModel(model)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table_view.horizontalHeader().setStretchLastSection(True)