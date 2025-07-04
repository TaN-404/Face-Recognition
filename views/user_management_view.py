from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTableView, 
                            QPushButton, QLineEdit, QComboBox, QLabel, 
                            QMessageBox, QHeaderView)
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, pyqtSignal

class UserManagementView(QWidget):
    # Define all signals at class level
    back_clicked = pyqtSignal()
    edit_user = pyqtSignal(dict)  # {uid, fname, lname}
    delete_user = pyqtSignal(str)  # uid
    search_requested = pyqtSignal(str, str)  # (search_text, search_type)
    clear_db_clicked = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setFixedSize(720, 1080)
        layout = QVBoxLayout(self)
        
        # Search Bar
        search_layout = QHBoxLayout()
        self.search_field = QLineEdit()
        self.search_field.setPlaceholderText("Search by UID or Name...")
        self.search_field.setFixedHeight(60)
        
        self.search_type = QComboBox()
        self.search_type.addItems(["UID", "First Name", "Last Name", "All"])
        self.search_type.setFixedWidth(140)
        
        search_btn = QPushButton("Search")
        search_btn.setFixedWidth(140)
        search_btn.clicked.connect(self.on_search_clicked)  # Changed method name
        
        search_layout.addWidget(self.search_field)
        search_layout.addWidget(self.search_type)
        search_layout.addWidget(search_btn)
        layout.addLayout(search_layout)
        
        # Results Table
        self.table_view = QTableView()
        self.table_view.setFixedSize(680, 680)
        self.table_view.setSelectionBehavior(QTableView.SelectRows)
        self.table_view.setSelectionMode(QTableView.SingleSelection)
        layout.addWidget(self.table_view)
        
        # Action Buttons
        btn_layout = QHBoxLayout()
        self.edit_btn = QPushButton("Edit User")
        self.edit_btn.setFixedHeight(60)
        self.edit_btn.setEnabled(False)
        
        self.delete_btn = QPushButton("Delete User")
        self.delete_btn.setFixedHeight(60)
        self.delete_btn.setEnabled(False)
        
        self.back_btn = QPushButton("Back")
        self.back_btn.setFixedHeight(60)
        self.back_btn.clicked.connect(self.back_clicked.emit)

        self.clear_db_btn = QPushButton("Clear Database")
        self.clear_db_btn.setFixedHeight(60)
        self.clear_db_btn.clicked.connect(self.clear_db_clicked.emit)

        
        btn_layout.addWidget(self.edit_btn)
        btn_layout.addWidget(self.delete_btn)
        btn_layout.addWidget(self.back_btn)
        layout.addLayout(btn_layout)

        layout.addWidget(self.clear_db_btn)
        
        # Initialize with empty model
        self.init_table()
        
        # Connect signals
        self.table_view.selectionModel().selectionChanged.connect(self.on_selection_changed)
        self.edit_btn.clicked.connect(self.on_edit_clicked)
        self.delete_btn.clicked.connect(self.on_delete_clicked)
    
    def init_table(self):
        """Initialize table with empty model"""
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["UID", "First Name", "Last Name"])
        self.table_view.setModel(self.model)
        
        # Column sizing
        header = self.table_view.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
    
    def display_users(self, users):
        """Display list of users in the table"""
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["UID", "First Name", "Last Name"])
        
        for user in users:
            if isinstance(user, dict):
                # Handle dictionary format
                items = [
                    QStandardItem(user['uid']),
                    QStandardItem(user['fname']),
                    QStandardItem(user['lname'])
                ]
            else:
                # Handle tuple format (assuming order: uid, fname, lname)
                items = [
                    QStandardItem(str(user[0])),
                    QStandardItem(user[1]),
                    QStandardItem(user[2])
                ]
            self.model.appendRow(items)
    
    def on_selection_changed(self):
        """Enable/disable action buttons based on selection"""
        selected = self.table_view.selectionModel().hasSelection()
        self.edit_btn.setEnabled(selected)
        self.delete_btn.setEnabled(selected)
    
    def on_search_clicked(self):
        """Handle search button click"""
        search_text = self.search_field.text().strip()
        search_type = self.search_type.currentText()
        self.search_requested.emit(search_text, search_type)
    
    def on_edit_clicked(self):
        """Handle edit button click"""
        index = self.table_view.selectionModel().currentIndex()
        uid = self.model.item(index.row(), 0).text()
        fname = self.model.item(index.row(), 1).text()
        lname = self.model.item(index.row(), 2).text()
        self.edit_user.emit({'uid': uid, 'fname': fname, 'lname': lname})
    
    def on_delete_clicked(self):
        """Handle delete button click"""
        index = self.table_view.selectionModel().currentIndex()
        uid = self.model.item(index.row(), 0).text()
        
        reply = QMessageBox.question(
            self, 'Confirm Delete',
            f"Delete user {uid}? This cannot be undone.",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            self.delete_user.emit(uid)
    
    def show_message(self, title, message):
        """Show information message"""
        QMessageBox.information(self, title, message)

    
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