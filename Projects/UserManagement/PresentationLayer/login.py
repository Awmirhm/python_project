from ttkbootstrap import Frame, Label, LabelFrame, Entry, Button, INFO, DARK, SUCCESS, OUTLINE, DANGER, WARNING, END
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.toast import ToastNotification
from BusinessLogicLayer.user_business import UserBusiness
from CommonLayer.logs_decorator import performance_logger_decorator


class LoginFrame(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.current_user = None

        self.view = view

        self.user_business = UserBusiness()

        self.grid_columnconfigure(0, weight=1)

        self.header = LabelFrame(self, text="Login Whit Your Account", bootstyle=WARNING)
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.header.grid_columnconfigure(1, weight=1)

        self.username_label = Label(self.header, text="Username : ", foreground="gray")
        self.username_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.username_entry = Entry(self.header, bootstyle=INFO, foreground="white")
        self.username_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        self.password_label = Label(self.header, text="Password : ", foreground="gray")
        self.password_label.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.password_entry = Entry(self.header, bootstyle=INFO, foreground="white", show="*")
        self.password_entry.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        self.login_button = Button(self.header, bootstyle=OUTLINE + INFO, text="Login",
                                   command=self.login_button_clicked)
        self.login_button.grid(row=2, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

        self.singing_button = Button(self.header, text="Sign in", command=self.singing_button_clicked,
                                     bootstyle=DANGER + OUTLINE)
        self.singing_button.grid(row=3, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

    @performance_logger_decorator()
    def login_button_clicked(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        result = self.user_business.login(username, password)
        user = result[0]
        self.current_user = user
        error_message = result[1]

        if error_message:
            Messagebox.show_error(error_message, title="Error", alert=True)
        else:
            toast_message = ToastNotification(title="Message",
                                              message=f"Hello {user.firstname} {user.lastname}"
                                                      f", Wellcome to Our Application",
                                              bootstyle=SUCCESS, position="SW", duration=5000, alert=True)
            toast_message.show_toast()

            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
            home_frame = self.view.switch("home")
            home_frame.set_current_user(user)

    @performance_logger_decorator()
    def singing_button_clicked(self):
        self.view.switch("sign_in")
