from PyQt5.QtCore import QTimer
from models.user_model import UserModel

class UserListPresenter:
    def __init__(self, view, navigator):
        self.view = view
        self.navigator = navigator
        self.user_model = UserModel()

        # Connect signals
        self.view.home_btn_clicked.connect(self.go_to_home)
        self.view.back_btn_clicked.connect(self.go_back)
        
        # Initialize data
        self.load_data()

    def load_data(self):
        """Load and display login history data"""
        try:
            users = self.user_model.get_all_users()
            if users:  # Only display if we have data
                self.view.display_data(users)
            else:
                print("No login history entries found")
        except Exception as e:
            print(f"Error loading login history: {e}")
            # You could show an error message in the UI here

    def go_to_home(self):
        """Handle navigation back to home"""
        self.navigator("home")

    def go_back(self):
        self.navigator("option")