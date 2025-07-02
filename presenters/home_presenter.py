class HomePresenter:
    def __init__(self, view, navigator):
        self.view = view
        self.navigator = navigator  # function to change screens

        self.view.new_user_clicked.connect(self.go_to_new_user)
        self.view.view_users_clicked.connect(self.go_to_users)  # for now

        self.view.start_camera()

    def go_to_new_user(self):
        self.view.stop_camera()
        self.navigator("new_user")

    def go_to_users(self):
        self.view.stop_camera()
        self.navigator("users")  # placeholder
