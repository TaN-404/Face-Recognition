from PyQt5.QtCore import QTimer
from models.history_model import LoginHistoryModel

class LoginHistoryPresenter:
    def __init__(self, view, navigator):
        self.view = view
        self.navigator = navigator
        self.history_model = LoginHistoryModel()

        # Connect signals
        self.view.home_btn_clicked.connect(self.go_to_home)
        
        # Initialize data
        self.load_data()

    def load_data(self):
        """Load and display login history data"""
        try:
            entries = self.history_model.get_all_entries()
            if entries:  # Only display if we have data
                self.view.display_data(entries)
            else:
                print("No login history entries found")
        except Exception as e:
            print(f"Error loading login history: {e}")
            # You could show an error message in the UI here

    def go_to_home(self):
        """Handle navigation back to home"""
        print("Back button pressed")
        self.navigator("home")