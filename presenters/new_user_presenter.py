from models.user_model import UserModel

class NewUserPresenter:
    def __init__(self, view, navigator):
        self.view = view
        self.navigator = navigator  # function like navigator("capture", user_data)
        self.user_model = UserModel()

        self.view.proceed_clicked.connect(self.on_proceed)
        self.view.back_clicked.connect(self.go_back)

    def on_proceed(self, user_data):
        # Basic validation
        uids = self.user_model.get_all_uid()
        if not user_data["fname"] or not user_data["lname"] or not user_data["uid"]:
            message = "All fields required"
            self.view.warning(message)
            return
        
        else:
            uid_list  = [item[0] for item in uids]
            for id in range(len(uid_list)):
                print(id)
                print(user_data["uid"])
                if user_data["uid"] == uid_list[id]:
                    message = "User Id exists"
                    self.view.warning(message)
                    return


        self.navigator("capture", user_data)  # Pass user data to capture presenter

    def go_back(self):
        self.navigator("home")
