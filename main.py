import sys
from insightface.app import FaceAnalysis
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget
from PyQt5.QtWidgets import QLabel

from PyQt5.QtGui import QPixmap, QImage, QMovie
from PyQt5.QtCore import QTimer, pyqtSignal, Qt


"""UI"""
from ui.theme_manager import apply_theme

"""OVERLAYS"""
from overlay.loading_overlay import LoadingOverlay


"""VIEWS"""
from views.home_view import HomeView
from views.new_user_view import NewUserView
from views.capture_view import CaptureView
from views.success_view import SuccessView
from views.option_view import OptionView
from views.login_history_view import LoginHistoryView
from views.user_list_view import UserListView
from views.user_management_view import UserManagementView
from views.edit_user_view import EditUserView
from views.fail_view import FailView



"""PRESENTERS"""
from presenters.new_user_presenter import NewUserPresenter
from presenters.home_presenter import HomePresenter
from presenters.capture_presenter import CapturePresenter
from presenters.success_presenter import SuccessPresenter
from presenters.option_presenter import OptionPresenter
from presenters.login_history_presenter import LoginHistoryPresenter
from presenters.user_list_presenter import UserListPresenter
from presenters.user_management_presenter import UserManagementPresenter
from presenters.edit_user_presenter import EditUserPresenter
from presenters.fail_presenter import FailPresenter

# Other views/presenters will be imported as you build them

class MainWindow(QWidget):
    def __init__(self):
        with open("ui/style.qss", "r") as f:
            app.setStyleSheet(f.read())

        super().__init__()
        self.setWindowTitle("Face Recognition")
        self.setFixedSize(720, 1080)

        self.stack = QStackedWidget()
        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)

        # Instantiate views
        self.home_view = HomeView()
        self.stack.addWidget(self.home_view)
        self.home_presenter = HomePresenter(self.home_view, self.switch_page)

        # self.loading_overlay = LoadingOverlay(self)
        # self.loading_overlay.setFixedSize(self.size())
        # self.loading_overlay.hide()
        # self.loading_overlay.lower() 

    def switch_page(self, page_name, data=None):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            if page_name == "home":
                self.home_view = HomeView()
                self.stack.addWidget(self.home_view)
                self.stack.setCurrentWidget(self.home_view)
                self.home_presenter.start_camera()
                self.home_presenter = HomePresenter(self.home_view, self.switch_page)


            elif page_name == "new_user":
                self.new_user_view = NewUserView()
                self.stack.addWidget(self.new_user_view)
                self.stack.setCurrentWidget(self.new_user_view)
                self.new_user_view.clear_fields()
                self.new_user_presenter = NewUserPresenter(self.new_user_view, self.switch_page)


            elif page_name == "capture":
                self.capture_view = CaptureView()
                self.stack.addWidget(self.capture_view)
                self.stack.setCurrentWidget(self.capture_view)
                self.capture_presenter = CapturePresenter(self.capture_view, self.switch_page, data)


            elif page_name == "success":
                self.success_view = SuccessView(data)
                self.stack.addWidget(self.success_view)
                self.stack.setCurrentWidget(self.success_view)
                self.succes_presenter = SuccessPresenter(self.success_view, self.switch_page, data)


            elif page_name == "fail":
                self.fail_view = FailView(data)
                self.stack.addWidget(self.fail_view)
                self.stack.setCurrentWidget(self.fail_view)
                self.fail_presenter = FailPresenter(self.fail_view, self.switch_page, data)


            elif page_name == "option":
                self.option_view = OptionView()
                self.stack.addWidget(self.option_view)
                self.stack.setCurrentWidget(self.option_view)
                self.option_presenter = OptionPresenter(self.option_view, self.switch_page)

            elif page_name == "login_history":
                self.login_history_view = LoginHistoryView()
                self.stack.addWidget(self.login_history_view)
                self.stack.setCurrentWidget(self.login_history_view)
                self.login_history_presenter = LoginHistoryPresenter(self.login_history_view, self.switch_page)
            
            elif page_name == "users_list":
                self.user_list_view = UserListView()
                self.stack.addWidget(self.user_list_view)
                self.stack.setCurrentWidget(self.user_list_view)
                self.user_list_presenter = UserListPresenter(self.user_list_view, self.switch_page)

            elif page_name == "user_management":
                self.user_management_view = UserManagementView()
                self.stack.addWidget(self.user_management_view)
                self.stack.setCurrentWidget(self.user_management_view)
                self.user_management_presenter = UserManagementPresenter(self.user_management_view,self.switch_page)

            elif page_name == "edit_user":
                self.edit_user_view = EditUserView(data)
                self.stack.addWidget(self.edit_user_view)
                self.stack.setCurrentWidget(self.edit_user_view)
                self.edit_user_presenter = EditUserPresenter(self.edit_user_view, self.switch_page, data)
        finally:
            QApplication.restoreOverrideCursor()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_theme(app, "light")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
