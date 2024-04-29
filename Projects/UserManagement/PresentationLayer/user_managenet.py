from ttkbootstrap import Frame, Treeview, Label, Button, INFO, LIGHT, DANGER, SUCCESS, OUTLINE, END, WARNING, DARK, \
    Combobox, StringVar, READONLY, Scrollbar, VERTICAL
from ttkbootstrap.dialogs import Messagebox
from BusinessLogicLayer.user_business import UserBusiness
from CommonLayer.logs_decorator import performance_logger_decorator


class UserManagement(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.user_business = UserBusiness()

        self.view = view

        self.current_user = None

        self.treeview = []

        self.super_admin_button = None
        self.admin_button = None
        self.default_user_button = None

        self.delete_button = None

        self.sort = None

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.header = Label(self, text="User Management", foreground="gray")
        self.header.grid(row=0, column=0, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="w")

        self.active_button = Button(self, text="Active", command=self.active_button_clicked,
                                    bootstyle=SUCCESS + OUTLINE)
        self.active_button.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="e")

        self.deactive_button = Button(self, text="Deactivate", bootstyle=DANGER + OUTLINE,
                                      command=self.deactive_button_clicked)
        self.deactive_button.grid(row=1, column=1, padx=(10, 10), pady=(10, 10), sticky="w")

        self.back_to_home_page_button = Button(self, text="Back To Home Page", bootstyle=WARNING,
                                               command=self.back_to_home_page_button_clicked)
        self.back_to_home_page_button.grid(row=5, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        # For Sort
        self.sort_combobox_var = StringVar(value="None")
        self.sort_combobox = Combobox(self, values=["Name", "Gender", "Age", "Role"],
                                      textvariable=self.sort_combobox_var, state=READONLY, bootstyle=DARK)

        self.sort_combobox.grid(row=5, column=0, columnspan=2, padx=(10, 10), pady=(10, 10))

        self.sort_button = Button(self, bootstyle=DARK, text=f"Sort By {self.sort_combobox_var.get()}",
                                  command=self.sort_button_clicked)
        self.sort_button.grid(row=6, column=0, columnspan=2, padx=(10, 10), pady=(10, 10))
        #

        self.y_scrollbar = Scrollbar(self, orient=VERTICAL, bootstyle=INFO)
        self.y_scrollbar.grid(row=4, column=2, padx=10, sticky="ns")

        self.columns = (
            "first_name", "last_name", "username", "email", "gender", "age", "country", "city", "status", "role")

        self.tabel = Treeview(self, columns=self.columns, bootstyle=INFO, yscrollcommand=self.y_scrollbar.set)

        self.y_scrollbar.config(command=self.tabel.yview)

        self.tabel.heading("#0", text="NO")
        self.tabel.heading("first_name", text="First Name")
        self.tabel.heading("last_name", text="Last Name")
        self.tabel.heading("username", text="Username")
        self.tabel.heading("email", text="Email")
        self.tabel.heading("gender", text="Gender")
        self.tabel.heading("age", text="Age")
        self.tabel.heading("country", text="Country")
        self.tabel.heading("city", text="City")
        self.tabel.heading("status", text="Status")
        self.tabel.heading("role", text="Role")

        self.tabel.grid(row=4, column=0, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="nsew")

    @performance_logger_decorator()
    def load_data(self, current_user):
        for item in self.treeview:
            self.tabel.delete(item)
        self.treeview.clear()

        self.current_user = current_user
        result = self.user_business.get_users(self.current_user, self.sort)
        users = result[0]
        error_message = result[1]

        if error_message:
            Messagebox.show_error(error_message, "Error", alert=True)
        else:
            row_number = 1
            for item in users:
                items = self.tabel.insert("", END, iid=item.username, text=str(row_number), values=(
                    item.firstname,
                    item.lastname,
                    item.username,
                    item.email,
                    "Male" if item.gender_id == 1 else "Female",
                    item.age,
                    item.country,
                    item.city,
                    "Active" if item.active == 1 else "Deactivate",
                    "Manager" if item.role_id == 1 else "Super Admin" if item.role_id == 2 else "Admin" if item.role_id
                                                                                                           == 3 else "Default User"
                ))

                row_number += 1
                self.treeview.append(items)

            self.tabel.column("#0", width=180, anchor="w")
            for column in self.columns:
                self.tabel.column(column, width=300, anchor="center")
        # For Manager
        if self.current_user.role_id == 1:
            if not self.super_admin_button:
                self.super_admin_button = Button(self, text="Click To Super Admin", bootstyle=OUTLINE + WARNING,
                                                 command=self.super_admin_button_clicked)
                self.super_admin_button.grid(row=3, column=0, columnspan=2, padx=(10, 10), pady=(0, 10))
        else:
            if self.super_admin_button:
                self.super_admin_button.destroy()
                self.super_admin_button = None
        # Delete For Manager
        if self.current_user.role_id == 1:
            if not self.delete_button:
                self.delete_button = Button(self, text="Delete User", bootstyle=DANGER,
                                            command=self.delete_button_clicked)
                self.delete_button.grid(row=5, column=1, padx=(10, 10), pady=(10, 10), sticky="e")
        else:
            if self.delete_button:
                self.delete_button.destroy()
                self.delete_button = None
        # For Manager & Super Admin
        if self.current_user.role_id == 1 or self.current_user.role_id == 2:
            if not self.admin_button or self.default_user_button:
                self.admin_button = Button(self, text="Click To Admin", bootstyle=OUTLINE + SUCCESS,
                                           command=self.admin_button_clicked)
                self.admin_button.grid(row=2, column=0, padx=(10, 10), pady=(0, 10), sticky="e")

                self.default_user_button = Button(self, text="Click To Default User", bootstyle=OUTLINE + DANGER,
                                                  command=self.default_user_button_clicked)
                self.default_user_button.grid(row=2, column=1, padx=(10, 10), pady=(0, 10), sticky="w")
        else:
            if self.admin_button and self.default_user_button:
                self.admin_button.destroy()
                self.default_user_button.destroy()
                self.admin_button = None
                self.default_user_button = None

    @performance_logger_decorator()
    def back_to_home_page_button_clicked(self):
        self.view.switch("home")

    @performance_logger_decorator()
    def active_button_clicked(self):
        for username_user in self.tabel.selection():
            error_message = self.user_business.update_to_active(self.current_user, username_user)

            if error_message:
                Messagebox.show_error(error_message, "Error", alert=True)
            else:
                self.load_data(self.current_user)

    @performance_logger_decorator()
    def deactive_button_clicked(self):
        for username_user in self.tabel.selection():
            error_message = self.user_business.update_to_deactivate(self.current_user, username_user)

            if error_message:
                Messagebox.show_error(error_message, title="Error", alert=True)
            else:
                self.load_data(self.current_user)

    @performance_logger_decorator()
    def super_admin_button_clicked(self):
        for username_user in self.tabel.selection():
            error_message = self.user_business.update_to_super_admin(self.current_user, username_user)

            if error_message:
                Messagebox.show_error(error_message, title="Error", alert=True)
            else:
                self.load_data(self.current_user)

    @performance_logger_decorator()
    def admin_button_clicked(self):
        for username_user in self.tabel.selection():
            error_message = self.user_business.update_to_admin(self.current_user, username_user)

            if error_message:
                Messagebox.show_error(error_message, title="Error", alert=True)
            else:
                self.load_data(self.current_user)

    @performance_logger_decorator()
    def default_user_button_clicked(self):
        for username_user in self.tabel.selection():
            error_message = self.user_business.update_to_default_user(self.current_user, username_user)

            if error_message:
                Messagebox.show_error(error_message, title="Error", alert=True)
            else:
                self.load_data(self.current_user)

    @performance_logger_decorator()
    def delete_button_clicked(self):
        for username_user in self.tabel.selection():
            error_message = self.user_business.delete_user(self.current_user, username_user)

            if error_message:
                Messagebox.show_error(error_message, "Error", alert=True)
            else:
                self.load_data(self.current_user)

    @performance_logger_decorator()
    def sort_button_clicked(self):
        sort_by = self.sort_combobox_var.get()
        if sort_by == "Name":
            self.sort_button.config(text=f"Sort by {self.sort_combobox_var.get()}")
            self.sort = "Name"
        if sort_by == "Gender":
            self.sort_button.config(text=f"Sort by {self.sort_combobox_var.get()}")
            self.sort = "Gender"
        if sort_by == "Age":
            self.sort_button.config(text=f"Sort by {self.sort_combobox_var.get()}")
            self.sort = "Age"
        if sort_by == "Role":
            self.sort_button.config(text=f"Sort by {self.sort_combobox_var.get()}")
            self.sort = "Role"
        self.load_data(self.current_user)
