class NewUserPresenter:
    def __init__(self, view, navigator):
        self.view = view
        self.navigator = navigator  # function like navigator("capture", user_data)

        self.view.proceed_clicked.connect(self.on_proceed)
        self.view.back_clicked.connect(self.go_back)

    def on_proceed(self, user_data):
        # Basic validation
        print("proceed pressed")
        if not user_data["fname"] or not user_data["lname"] or not user_data["uid"]:
            print("⚠️ All fields required")
            return

        self.navigator("capture", user_data)  # Pass user data to capture presenter

    def go_back(self):
        self.navigator("home")
