from ttkbootstrap import Frame, Button, Label, Entry, Labelframe, Separator, HORIZONTAL, VERTICAL, INFO, READONLY, \
    StringVar, WARNING, DANGER, OUTLINE, LIGHT
from ttkbootstrap.dialogs import Messagebox
from BusinessLogicLayer.user_business import UserBusiness
from CommonLayer.logs_decorator import performance_logger_decorator


class ProfileFame(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.current_user = None

        self.view = view

        self.user_business = UserBusiness()

        self.grid_columnconfigure(0, weight=1)

        self.header = Labelframe(self, text="Your Profile", bootstyle=INFO)
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.firstname_label = Label(self.header, text="First Name : ")
        self.firstname_label.grid(row=0, column=0, padx=(10, 0), pady=(10, 10), sticky="w")

        self.firstname_entry_var = StringVar(value="")
        self.firstname_entry = Entry(self.header, state=READONLY, textvariable=self.firstname_entry_var)
        self.firstname_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="w")

        self.sep_vertical = Separator(self.header, orient=VERTICAL, bootstyle=WARNING)
        self.sep_vertical.grid(row=0, column=2, padx=(5, 5), pady=(10, 10), sticky="ns")

        self.lastname_label = Label(self.header, text="Last Name : ")
        self.lastname_label.grid(row=0, column=3, padx=(10, 0), pady=(10, 10), sticky="w")

        self.lastname_entry_var = StringVar(value="")
        self.lastname_entry = Entry(self.header, state=READONLY, textvariable=self.lastname_entry_var)
        self.lastname_entry.grid(row=0, column=4, padx=(0, 10), pady=(10, 10), sticky="w")

        self.sep_horizontal = Separator(self.header, orient=HORIZONTAL, bootstyle=DANGER)
        self.sep_horizontal.grid(row=1, column=0, padx=(5, 5), pady=(0, 0), sticky="ew")

        self.username_label = Label(self.header, text="Username : ")
        self.username_label.grid(row=2, column=0, padx=(10, 0), pady=(10, 10), sticky="w")

        self.username_entry_var = StringVar(value="")
        self.username_entry = Entry(self.header, state=READONLY, textvariable=self.username_entry_var)
        self.username_entry.grid(row=2, column=1, padx=(0, 10), pady=(10, 10), sticky="w")

        self.sep_vertical_2 = Separator(self.header, orient=VERTICAL, bootstyle=WARNING)
        self.sep_vertical_2.grid(row=2, column=2, padx=(5, 5), pady=(10, 10), sticky="ns")

        self.email_label = Label(self.header, text="Email : ")
        self.email_label.grid(row=2, column=3, padx=(10, 0), pady=(10, 10), sticky="w")

        self.email_entry_var = StringVar(value="")
        self.email_entry = Entry(self.header, state=READONLY, textvariable=self.email_entry_var)
        self.email_entry.grid(row=2, column=4, padx=(0, 10), pady=(10, 10), sticky="w")

        self.sep_horizontal_2 = Separator(self.header, orient=HORIZONTAL, bootstyle=DANGER)
        self.sep_horizontal_2.grid(row=1, column=3, padx=(5, 5), pady=(0, 0), sticky="ew")

        self.sep_horizontal_3 = Separator(self.header, orient=HORIZONTAL, bootstyle=DANGER)
        self.sep_horizontal_3.grid(row=3, column=0, padx=(5, 5), pady=(0, 0), sticky="ew")

        self.gender_label = Label(self.header, text="Gender : ")
        self.gender_label.grid(row=4, column=0, padx=(10, 0), pady=(10, 10), sticky="w")

        self.gender_entry_var = StringVar(value="")
        self.gender_entry = Entry(self.header, state=READONLY, textvariable=self.gender_entry_var)
        self.gender_entry.grid(row=4, column=1, padx=(0, 10), pady=(10, 10), sticky="w")

        self.sep_vertical_3 = Separator(self.header, orient=VERTICAL, bootstyle=WARNING)
        self.sep_vertical_3.grid(row=4, column=2, padx=(5, 5), pady=(10, 10), sticky="ns")

        self.age_label = Label(self.header, text="Age : ")
        self.age_label.grid(row=4, column=3, padx=(10, 0), pady=(10, 10), sticky="w")

        self.age_entry_var = StringVar(value="")
        self.age_entry = Entry(self.header, state=READONLY, textvariable=self.age_entry_var)
        self.age_entry.grid(row=4, column=4, padx=(0, 10), pady=(10, 10), sticky="w")

        self.sep_horizontal_4 = Separator(self.header, orient=HORIZONTAL, bootstyle=DANGER)
        self.sep_horizontal_4.grid(row=3, column=3, padx=(5, 5), pady=(0, 0), sticky="ew")

        self.sep_horizontal_5 = Separator(self.header, orient=HORIZONTAL, bootstyle=DANGER)
        self.sep_horizontal_5.grid(row=5, column=0, padx=(5, 5), pady=(0, 0), sticky="ew")

        self.country_label = Label(self.header, text="Country : ")
        self.country_label.grid(row=6, column=0, padx=(10, 0), pady=(10, 10), sticky="w")

        self.country_entry_var = StringVar(value="")
        self.country_entry = Entry(self.header, state=READONLY, textvariable=self.country_entry_var)
        self.country_entry.grid(row=6, column=1, padx=(0, 10), pady=(10, 10), sticky="w")

        self.sep_vertical_4 = Separator(self.header, orient=VERTICAL, bootstyle=WARNING)
        self.sep_vertical_4.grid(row=6, column=2, padx=(5, 5), pady=(10, 10), sticky="ns")

        self.city_label = Label(self.header, text="City : ")
        self.city_label.grid(row=6, column=3, padx=(10, 0), pady=(10, 10), sticky="w")

        self.sep_horizontal_6 = Separator(self.header, orient=HORIZONTAL, bootstyle=DANGER)
        self.sep_horizontal_6.grid(row=5, column=3, padx=(5, 5), pady=(0, 0), sticky="ew")

        self.city_entry_var = StringVar(value="")
        self.city_entry = Entry(self.header, state=READONLY, textvariable=self.city_entry_var)
        self.city_entry.grid(row=6, column=4, padx=(0, 10), pady=(10, 10), sticky="w")

        self.sep_horizontal_7 = Separator(self.header, orient=HORIZONTAL, bootstyle=DANGER)
        self.sep_horizontal_7.grid(row=7, column=0, padx=(5, 5), pady=(0, 0), sticky="ew")

        self.status_label = Label(self.header, text="Status : ")
        self.status_label.grid(row=8, column=0, padx=(10, 0), pady=(10, 10), sticky="w")

        self.status_entry_var = StringVar(value="")
        self.status_entry = Entry(self.header, state=READONLY, textvariable=self.status_entry_var)
        self.status_entry.grid(row=8, column=1, padx=(0, 10), pady=(10, 10), sticky="w")

        self.sep_vertical_5 = Separator(self.header, orient=VERTICAL, bootstyle=WARNING)
        self.sep_vertical_5.grid(row=8, column=2, padx=(5, 5), pady=(10, 10), sticky="ns")

        self.sep_horizontal_8 = Separator(self.header, orient=HORIZONTAL, bootstyle=DANGER)
        self.sep_horizontal_8.grid(row=7, column=3, padx=(5, 5), pady=(0, 0), sticky="ew")

        self.role_label = Label(self.header, text="Role : ")
        self.role_label.grid(row=8, column=3, padx=(10, 0), pady=(10, 10), sticky="w")

        self.role_entry_var = StringVar(value="")
        self.role_entry = Entry(self.header, state=READONLY, textvariable=self.role_entry_var)
        self.role_entry.grid(row=8, column=4, padx=(0, 10), pady=(10, 10), sticky="w")

        self.back_to_home_page_button = Button(self, text="Back To Home Page", bootstyle=WARNING + OUTLINE,
                                               command=self.back_to_home_page_button_clicked)
        self.back_to_home_page_button.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.edit_information_button = Button(self, text="Edit Information",
                                              command=self.edit_information_button_clicked, bootstyle=OUTLINE + LIGHT)
        self.edit_information_button.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="e")

    @performance_logger_decorator()
    def set_current_user_for_profile_frame(self, current_user):
        self.current_user = current_user
        result = self.user_business.profile(self.current_user)
        user = result[0]
        error_message = result[1]

        if error_message:
            Messagebox.show_error(title="Error", message=error_message, alert=True)
        else:
            self.firstname_entry_var.set(f"{user.firstname}")

            self.lastname_entry_var.set(f"{user.lastname}")

            self.username_entry_var.set(f"{user.username}")

            self.email_entry_var.set(f"{user.email}")

            self.gender_entry_var.set(f"{"Male" if user.gender_id == 1 else "Female"}")

            self.age_entry_var.set(f"{user.age}")

            self.country_entry_var.set(f"{user.country}")

            self.city_entry_var.set(f"{user.city}")

            self.status_entry_var.set(f"{"Active" if user.active == 1 else "Deactivate"}")

            self.role_entry_var.set(f"{"Manager" if user.role_id == 1 else "Super Admin" if user.role_id == 2
            else "Admin" if user.role_id == 3 else "Default User"}")

    @performance_logger_decorator()
    def back_to_home_page_button_clicked(self):
        self.view.switch("home")

    @performance_logger_decorator()
    def edit_information_button_clicked(self):
        edit_information_frame = self.view.switch("edit")
        edit_information_frame.set_current_user_for_edit_information_frame(self.current_user)
