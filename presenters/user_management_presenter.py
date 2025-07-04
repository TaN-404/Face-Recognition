from PyQt5.QtCore import QObject
from models.user_model import UserModel  # Assuming you have a user model

class UserManagementPresenter(QObject):
    def __init__(self, view, navigator):
        super().__init__()
        self.view = view
        self.navigator = navigator
        self.user_model = UserModel()
        
        # Connect signals
        self.view.back_clicked.connect(self.go_back)
        self.view.search_requested.connect(self.handle_search)
        self.view.edit_user.connect(self.handle_edit)
        self.view.delete_user.connect(self.handle_delete)
        self.view.clear_db_clicked.connect(self.clear_db)


        # Initial load
        self.load_all_users()
    
    def load_all_users(self):
        users = self.user_model.get_all_users()
        self.view.display_users(users)
        print(users)
    
    def handle_search(self, text, search_type):
        if not text:
            self.load_all_users()
            return
            
        if search_type == "UID":
            users = self.user_model.search_by_uid(text)
        elif search_type == "First Name":
            users = self.user_model.search_by_fname(text)
        elif search_type == "Last Name":
            users = self.user_model.search_by_lname(text)
        else:  # "All"
            users = self.user_model.search_all_fields(text)
            
        self.view.display_users(users)
    
    def handle_edit(self, user_data):
        # Navigate to edit page with user data
        self.navigator("edit_user", user_data)
    
    def handle_delete(self, uid):
        success = self.user_model.delete_user(uid)
        if success:
            self.view.show_message("Success", f"User {uid} deleted successfully")
            self.load_all_users()
        else:
            self.view.show_message("Error", "Failed to delete user")
    

    def clear_db(self):
        if self.view.confirm_action():
            self.user_model.drop_user_table()

            
    def go_back(self):
        self.navigator("option")  # Or wherever you want to go back to