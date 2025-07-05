from PyQt5.QtCore import QTimer
from models.history_model import LoginHistoryModel

class LoginHistoryPresenter:
    def __init__(self, view, navigator):
        self.view = view
        self.navigator = navigator
        self.history_model = LoginHistoryModel()
        

        # Connect signals
        self.view.home_btn_clicked.connect(self.go_to_home)
        self.view.back_btn_clicked.connect(self.go_back)
        self.view.clear_history_clicked.connect(self.clear_history)
        
        # Initialize data
        self.load_data()

    def clear_history(self):
        if self.view.confirm_action():
            self.history_model.clear_login_history()
            self.navigator("login_history")
            # entries = self.load_data()
            # self.view.display_data(entries)

    def load_data(self):
        """Load and display login history data"""
        try:
            entries = self.history_model.get_all_entries()
            if entries:  # Only display if we have data
                self.view.display_data(entries)
                # return entries
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