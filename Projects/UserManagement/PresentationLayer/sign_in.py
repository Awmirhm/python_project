from ttkbootstrap import Frame, Labelframe, Label, Entry, Button, Combobox, Radiobutton, StringVar, INFO, WARNING, \
    SUCCESS, LIGHT, DARK, DANGER, READONLY, OUTLINE, END, Spinbox
from ttkbootstrap.dialogs import Messagebox
from BusinessLogicLayer.user_business import UserBusiness
from CommonLayer.country import CountrySelection
from CommonLayer.logs_decorator import performance_logger_decorator


class SigninFrame(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.view = view

        self.user_business = UserBusiness()

        #   For Country
        self.country_selection = CountrySelection()
        self.country_list = self.country_selection.get_all_country()
        #

        self.grid_columnconfigure(0, weight=1)

        self.header = Labelframe(self, text="Create Your Account", bootstyle=SUCCESS)
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.header.grid_columnconfigure(1, weight=1)

        self.firstname_label = Label(self.header, text="First Name : ", foreground="gray")
        self.firstname_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.firstname_entry = Entry(self.header, bootstyle=DARK)
        self.firstname_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        self.lastname_label = Label(self.header, text="Last Name : ", foreground="gray")
        self.lastname_label.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.lastname_entry = Entry(self.header, bootstyle=DARK)
        self.lastname_entry.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        self.username_label = Label(self.header, text="Username : ", foreground="gray")
        self.username_label.grid(row=2, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.username_entry = Entry(self.header, bootstyle=DARK)
        self.username_entry.grid(row=2, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        self.password_label = Label(self.header, text="Password : ", foreground="gray")
        self.password_label.grid(row=3, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.password_entry = Entry(self.header, bootstyle=DARK)
        self.password_entry.grid(row=3, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        self.repeat_password_label = Label(self.header, text="Repeat your password : ", foreground="gray")
        self.repeat_password_label.grid(row=4, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.repeat_password_entry = Entry(self.header, bootstyle=DARK)
        self.repeat_password_entry.grid(row=4, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        self.email_label = Label(self.header, text="Email : ", foreground="gray")
        self.email_label.grid(row=5, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.email_entry = Entry(self.header, bootstyle=DARK)
        self.email_entry.grid(row=5, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        self.age_label = Label(self.header, text="Age : ", foreground="gray")
        self.age_label.grid(row=6, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.age_spinbox = Spinbox(self.header, from_=0, to=100, wrap=True, bootstyle=DARK)
        self.age_spinbox.grid(row=6, column=1, padx=(0, 10), pady=(0, 10), sticky="w")
        # For Gender
        self.gender_label = Label(self.header, text="Gender : ", foreground="gray")
        self.gender_label.grid(row=7, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.gender_radio_button_var = StringVar(value="0")

        self.gender_radio_button_for_male = Radiobutton(self.header, value=1, text="Male",
                                                        variable=self.gender_radio_button_var, bootstyle=INFO)
        self.gender_radio_button_for_male.grid(row=7, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

        self.gender_radio_button_for_female = Radiobutton(self.header, value=2, text="Female",
                                                          variable=self.gender_radio_button_var, bootstyle=DANGER)
        self.gender_radio_button_for_female.grid(row=7, column=1, padx=(80, 10), pady=(0, 10), sticky="w")
        #

        # For Country Combobox and City Entry
        self.country_label = Label(self.header, text="Country : ", foreground="gray")
        self.country_label.grid(row=8, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.country_combobox_var = StringVar()

        self.country_combobox = Combobox(self.header, values=self.country_list, state=READONLY,
                                         textvariable=self.country_combobox_var, bootstyle=DARK)
        self.country_combobox.grid(row=8, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

        self.city_label = Label(self.header, text="City : ", foreground="gray")
        self.city_label.grid(row=9, column=0, padx=(10, 10), pady=(0, 10))

        self.city_entry = Entry(self.header, bootstyle=DARK)
        self.city_entry.grid(row=9, column=1, padx=(0, 10), pady=(0, 10), sticky="w")
        #

        self.save_button = Button(self.header, text="Save", bootstyle=OUTLINE + INFO,
                                  command=self.save_to_create_account)
        self.save_button.grid(row=10, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

        self.back_to_login_page_button = Button(self, text="Back To Login Page", bootstyle=WARNING,
                                                command=self.back_to_login_page_button_clicked)
        self.back_to_login_page_button.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")

    @performance_logger_decorator()
    def save_to_create_account(self):
        firstname = self.firstname_entry.get()
        lastname = self.lastname_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        repeat_password = self.repeat_password_entry.get()
        email = self.email_entry.get()
        age = int(self.age_spinbox.get())
        gender = self.gender_radio_button_var.get()
        country = self.country_combobox_var.get()
        city = self.city_entry.get()

        result = self.user_business.signin(firstname=firstname, lastname=lastname, username=username,
                                           password=password, repeat_password=repeat_password, email=email,
                                           gender=gender, age=age,
                                           country=country, city=city)
        save_message = result[0]
        error_message = result[1]

        if error_message:
            Messagebox.show_error(error_message, "Error", alert=True)
        else:
            Messagebox.show_info(save_message, "Info", alert=True)

    @performance_logger_decorator()
    def back_to_login_page_button_clicked(self):
        self.firstname_entry.delete(0, END)
        self.lastname_entry.delete(0, END)
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.repeat_password_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.age_spinbox.delete(0, END)
        self.country_combobox.delete(0, END)
        self.city_entry.delete(0, END)
        self.view.switch("login")
