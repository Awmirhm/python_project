from ttkbootstrap import Frame, Treeview, Label, Button, DANGER, END, WARNING, OUTLINE, Scrollbar, VERTICAL, LIGHT
from ttkbootstrap.dialogs import Messagebox
from BusinessLogicLayer.user_business import UserBusiness
from CommonLayer.logs_decorator import performance_logger_decorator


class LogFrame(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.user_business = UserBusiness()

        self.treeview_items = []

        self.view = view

        self.current_user = None

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.header = Label(self, text="Logs", foreground="gray")
        self.header.grid(row=0, column=0, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="w")

        self.back_to_home_page_button = Button(self, text="Back To Home Page", bootstyle=WARNING,
                                               command=self.back_to_home_page_button_clicked)
        self.back_to_home_page_button.grid(row=2, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.delete_button = Button(self, text="Delete", bootstyle=OUTLINE + DANGER, command=self.delete_button_clicked)
        self.delete_button.grid(row=2, column=0, padx=(10, 10), pady=(10, 10), sticky="e")

        self.y_scrollbar = Scrollbar(self, orient=VERTICAL, bootstyle=LIGHT)
        self.y_scrollbar.grid(row=1, column=1, padx=10, sticky="ns")

        self.columns = ("function_name", "call_data_time", "execution_time","username_clicker")

        self.table = Treeview(self, columns=self.columns, bootstyle=DANGER, yscrollcommand=self.y_scrollbar.set)

        self.y_scrollbar.config(command=self.table.yview)

        self.table.heading("#0", text="NO")
        self.table.heading("function_name", text="Function Name")
        self.table.heading("call_data_time", text="Call Data Time")
        self.table.heading("execution_time", text="Execution Time")
        self.table.heading("username_clicker", text="Username Clicker")

        self.table.grid(row=1, column=0, columnspan=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

    # @performance_logger_decorator()
    def load_logs(self, current_user):
        for item in self.treeview_items:
            self.table.delete(item)
        self.treeview_items.clear()

        self.current_user = current_user

        result = self.user_business.get_logs(self.current_user)
        logs = result[0]
        error_message = result[1]

        if error_message:
            Messagebox.show_error(title="Error", message=error_message, alert=True)
        else:
            row_number = 1
            for item in logs:
                items = self.table.insert("", END, iid=item.id, text=str(row_number), values=(
                    item.function_name,
                    item.call_data_time,
                    item.execution_time,
                    item.username_clicker
                ))
                row_number += 1

                self.treeview_items.append(items)

            self.table.column("#0", width=180, anchor="w")
            for column in self.columns:
                self.table.column(column, width=300, anchor="center")

    @performance_logger_decorator()
    def back_to_home_page_button_clicked(self):
        self.view.switch("home")

    @performance_logger_decorator()
    def delete_button_clicked(self):
        for log_id in self.table.selection():
            error_message = self.user_business.delete_for_log(self.current_user, log_id)

            if error_message:
                Messagebox.show_error(title="Error", alert=True, message=error_message)
            else:
                self.load_logs(self.current_user)
