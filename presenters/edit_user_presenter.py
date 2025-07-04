from PyQt5.QtCore import QObject
from models.user_model import UserModel

class EditUserPresenter(QObject):
    def __init__(self, view, navigator, user_data):
        super().__init__()
        self.view = view
        self.navigator = navigator
        self.user_model = UserModel()
        self.original_data = user_data
        
        # Connect signals
        self.view.back_clicked.connect(self.go_back)
        self.view.save_clicked.connect(self.handle_save)
    
    def handle_save(self, new_data):
        # Validate data
        if not new_data['fname'] or not new_data['lname']:
            self.view.show_message("Error", "Name fields cannot be empty")
            return
            
        # Update user
        success = self.user_model.update_user(
            self.original_data['uid'],
            new_data['fname'],
            new_data['lname']
        )
        
        if success:
            self.view.show_message("Success", "User updated successfully")
            self.navigator("user_management")
        else:
            self.view.show_message("Error", "Failed to update user")
    
    def go_back(self):
        self.navigator("user_management")