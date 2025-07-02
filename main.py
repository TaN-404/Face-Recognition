import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget
from PyQt5.QtWidgets import QLabel


"""VIEWS"""
from views.home_view import HomeView
from views.new_user_view import NewUserView
from views.capture_view import CaptureView


"""PRESENTERS"""
from presenters.new_user_presenter import NewUserPresenter
from presenters.home_presenter import HomePresenter
from presenters.capture_presenter import CapturePresenter

# Other views/presenters will be imported as you build them

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Face Recognition")
        self.setFixedSize(720, 1080)

        self.stack = QStackedWidget()
        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)

        # Instantiate views
        self.home_view = HomeView()
        self.stack.addWidget(self.home_view)  # index 0

        # Placeholder for new user

        self.new_user_view = NewUserView()
        self.stack.addWidget(self.new_user_view)

        self.users_placeholder = QLabel("Users Page (To Be Built)")
        self.stack.addWidget(self.users_placeholder)  # index 2

        self.capture_view = CaptureView()
        self.stack.addWidget(self.capture_view)


        # Connect presenter
        self.home_presenter = HomePresenter(self.home_view, self.switch_page)
        self.new_user_presenter = NewUserPresenter(self.new_user_view, self.switch_page)
        # self.capture_presenter = CapturePresenter(self.capture_view, self.switch_page)
        

    def switch_page(self, page_name, data=None):
        if page_name == "home":
            self.stack.setCurrentWidget(self.home_view)
            self.home_view.start_camera()
        elif page_name == "new_user":
            self.stack.setCurrentWidget(self.new_user_view)
            self.new_user_view.clear_fields()
        elif page_name == "capture":
            self.capture_view = CaptureView()
            self.stack.addWidget(self.capture_view)
            self.stack.setCurrentWidget(self.capture_view)
            self.capture_presenter = CapturePresenter(self.capture_view, self.switch_page, data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
