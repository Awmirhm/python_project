from ttkbootstrap import Frame, Labelframe, Label, Entry, Button, WARNING, INFO, DARK, OUTLINE, SUCCESS, Combobox, \
    StringVar, READONLY, END, Spinbox
from ttkbootstrap.dialogs import Messagebox
from BusinessLogicLayer.user_business import UserBusiness
from CommonLayer.country import CountrySelection
from CommonLayer.logs_decorator import performance_logger_decorator


class EditInformation(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.view = view

        self.current_user = None

        self.user_business = UserBusiness()

        self.country_selection = CountrySelection()
        self.all_country = self.country_selection.get_all_country()

        self.grid_columnconfigure(0, weight=1)

        self.header = Labelframe(self, text="Edit Information", bootstyle=INFO)
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.header.grid_columnconfigure(1, weight=1)

        self.new_firstname_label = Label(self.header, text="New First Name : ", foreground="gray")
        self.new_firstname_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.new_firstname_entry = Entry(self.header, bootstyle=DARK)
        self.new_firstname_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        self.new_lastname_label = Label(self.header, text="New Last Name : ", foreground="gray")
        self.new_lastname_label.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.new_lastname_entry = Entry(self.header, bootstyle=DARK)
        self.new_lastname_entry.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        self.new_username_label = Label(self.header, text="New Username : ", foreground="gray")
        self.new_username_label.grid(row=2, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.new_username_entry = Entry(self.header, bootstyle=DARK)
        self.new_username_entry.grid(row=2, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        self.new_email_label = Label(self.header, text="New Email : ", foreground="gray")
        self.new_email_label.grid(row=3, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.new_email_entry = Entry(self.header, bootstyle=DARK)
        self.new_email_entry.grid(row=3, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        self.new_age_label = Label(self.header, text="Age : ", foreground="gray")
        self.new_age_label.grid(row=4, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.new_age_spinbox = Spinbox(self.header, from_=0, to=100, wrap=True, bootstyle=DARK)
        self.new_age_spinbox.grid(row=4, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

        # Country & City
        self.country_label = Label(self.header, text="Country : ", foreground="gray")
        self.country_label.grid(row=5, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.country_combobox_var = StringVar()
        self.country_combobox = Combobox(self.header, values=self.all_country, textvariable=self.country_combobox_var,
                                         bootstyle=DARK, state=READONLY)
        self.country_combobox.grid(row=5, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

        self.city_label = Label(self.header, text="City : ", foreground="gray")
        self.city_label.grid(row=6, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.city_entry = Entry(self.header, bootstyle=DARK)
        self.city_entry.grid(row=6, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

        self.save_button = Button(self.header, text="Save", bootstyle=OUTLINE + SUCCESS,
                                  command=self.save_to_edit_information)
        self.save_button.grid(row=7, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

        self.back_to_home_page_button = Button(self, text="Back To Home Page", bootstyle=WARNING,
                                               command=self.back_to_home_page_button_clicked)
        self.back_to_home_page_button.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="ew")

    def set_current_user_for_edit_information_frame(self, current_user):
        self.current_user = current_user

    @performance_logger_decorator()
    def save_to_edit_information(self):
        new_firstname = self.new_firstname_entry.get()
        new_lastname = self.new_lastname_entry.get()
        new_username = self.new_username_entry.get()
        new_email = self.new_email_entry.get()
        new_age = self.new_age_spinbox.get()
        new_country = self.country_combobox_var.get()
        new_city = self.city_entry.get()

        result = self.user_business.edit_information(self.current_user, new_firstname, new_lastname, new_username,
                                                     new_email, new_age, new_country, new_city)
        save_message = result[0]
        error_message = result[1]

        if error_message:
            Messagebox.show_error(message=error_message, title="Error", alert=True)
        else:
            Messagebox.ok(message=save_message, title="Info", alert=True)

    @performance_logger_decorator()
    def back_to_home_page_button_clicked(self):
        self.new_firstname_entry.delete(0, END)
        self.new_lastname_entry.delete(0, END)
        self.new_username_entry.delete(0, END)
        self.new_email_entry.delete(0, END)
        self.country_combobox.delete(0, END)
        self.city_entry.delete(0, END)
        self.view.switch("home")
