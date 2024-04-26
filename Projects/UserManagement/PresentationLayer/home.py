from ttkbootstrap import Frame, Label, Button, OUTLINE, INFO, SUCCESS, WARNING, LIGHT, PRIMARY, DANGER
from CommonLayer.logs_decorator import performance_logger_decorator


class HomeFrame(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.view = view

        self.current_user = None

        self.user_management_button = None

        self.log_button = None

        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Wellcome", foreground="#00DFA2")
        self.header.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="w")

        self.profile_button = Button(self, text="Your Profile", bootstyle=OUTLINE + LIGHT,
                                     command=self.profile_button_clicked)
        self.profile_button.grid(row=3, column=1, padx=(10, 10), pady=(10, 10), sticky="ew")

        self.edit_information_button = Button(self, text="Edit Information", bootstyle=OUTLINE + SUCCESS,
                                              command=self.edit_information_button_clicked)
        self.edit_information_button.grid(row=4, column=1, padx=(10, 10), pady=(10, 10), sticky="ew")

        self.logout_button = Button(self, text="Logout", bootstyle=WARNING,
                                    command=self.logout_button_clicked)
        self.logout_button.grid(row=5, column=1, padx=(10, 10), pady=(10, 10), sticky="ew")

    @performance_logger_decorator()
    def logout_button_clicked(self):
        self.view.switch("login")

    @performance_logger_decorator()
    def set_current_user(self, user):
        self.current_user = user
        self.header.config(text=f"Wellcome, {self.current_user.firstname} {self.current_user.lastname}")
        # For Manager & Super Admin & Admin
        if self.current_user.role_id == 1 or self.current_user.role_id == 2 or self.current_user.role_id == 3:
            if not self.user_management_button:
                self.user_management_button = Button(self, text="User Management", bootstyle=INFO + OUTLINE,
                                                     command=self.show_user)
                self.user_management_button.grid(row=1, column=1, padx=(10, 10), pady=(10, 10), sticky="ew")
        else:
            if self.user_management_button:
                self.user_management_button.destroy()
                self.user_management_button = None
        # For Manager
        if self.current_user.role_id == 1:
            if not self.log_button:
                self.log_button = Button(self, text="Logs", bootstyle=OUTLINE + DANGER, command=self.log_button_clicked)
                self.log_button.grid(row=2, column=1, padx=(10, 10), pady=(10, 10), sticky="ew")
        else:
            if self.log_button:
                self.log_button.destroy()
                self.log_button = None

    @performance_logger_decorator()
    def show_user(self):
        user_management_frame = self.view.switch("user_management")
        user_management_frame.load_data(self.current_user)

    @performance_logger_decorator()
    def edit_information_button_clicked(self):
        edit_information_frame = self.view.switch("edit")
        edit_information_frame.set_current_user_for_edit_information_frame(self.current_user)

    @performance_logger_decorator()
    def profile_button_clicked(self):
        profile_frame = self.view.switch("profile")
        profile_frame.set_current_user_for_profile_frame(self.current_user)

    @performance_logger_decorator()
    def log_button_clicked(self):
        log_frame = self.view.switch("logs")
        log_frame.load_logs(self.current_user)
