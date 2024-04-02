from tkinter import Tk, Label, Button, Entry, END
import sqlite3
import random
import time

window = Tk()
window.title("Login to the Account")

username_label = Label(window, text="Username : ")
username_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

username_entry = Entry(window, width=30)
username_entry.grid(row=0, column=1, padx=(10, 10), pady=(10, 10))

password_label = Label(window, text="Password : ")
password_label.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

password_entry = Entry(window, width=30)
password_entry.grid(row=1, column=1, padx=(10, 10), pady=(10, 10))


def login_button_click():
    user = username_entry.get()
    password = password_entry.get()

    with sqlite3.connect("BankDB.db") as connection_6:
        cursor_6 = connection_6.cursor()
        data_6 = cursor_6.execute("""
                                    SELECT id,
                                           username,
                                           password
                                    FROM Bank_user;
                                    """).fetchall()
        for item_2 in data_6:
            if user == item_2[1] and password == item_2[2]:
                window.destroy()
                crate_table_bode_for_window_1()

            else:
                error_label = Label(window, text="Invalid Username or Password", fg="Maroon")
                error_label.grid(row=2, column=1, padx=(10, 10), pady=(10, 10))


def crate_table_bode_for_window_1():
    window_1 = Tk()
    window_1.title("People Account")

    row_label = Label(window_1, text="#")
    row_label.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

    bank_name_label = Label(window_1, text="Bank Name")
    bank_name_label.grid(row=1, column=1, padx=(10, 10), pady=(10, 10))

    account_number_label = Label(window_1, text="Account Number")
    account_number_label.grid(row=1, column=2, padx=(10, 10), pady=(10, 10))

    account_balance_label = Label(window_1, text="Account Balance")
    account_balance_label.grid(row=1, column=3, padx=(10, 10), pady=(10, 10))

    first_name_label = Label(window_1, text="First Name")
    first_name_label.grid(row=1, column=4, padx=(10, 10), pady=(10, 10))

    last_name_label = Label(window_1, text="Last Name")
    last_name_label.grid(row=1, column=5, padx=(10, 10), pady=(10, 10))

    national_code_label = Label(window_1, text="National Code")
    national_code_label.grid(row=1, column=6, padx=(10, 10), pady=(10, 10))
    time_label = Label(window_1, text=f"Entered on this date and time :\n {time.ctime()}", fg="white", bg="black")
    time_label.grid(row=1000, column=0, padx=(0, 0), pady=(10, 10))

    def create_account_button_click():
        window_2 = Tk()
        window_2.title("Create a Account")

        first_name_label_1 = Label(window_2, text="First Name : ")
        first_name_label_1.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

        first_name_entry_1 = Entry(window_2, width=30)
        first_name_entry_1.grid(row=0, column=1, padx=(10, 10), pady=(10, 10))

        last_name_label_1 = Label(window_2, text="Last Name : ")
        last_name_label_1.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

        last_name_entry_1 = Entry(window_2, width=30)
        last_name_entry_1.grid(row=1, column=1, padx=(10, 10), pady=(10, 10))

        national_code_label_1 = Label(window_2, text="National Code : ")
        national_code_label_1.grid(row=2, column=0, padx=(10, 10), pady=(10, 10))

        national_code_entry_1 = Entry(window_2, width=30)
        national_code_entry_1.grid(row=2, column=1, padx=(10, 10), pady=(10, 10))

        bank_name_label_1 = Label(window_2, text="Bank Name : ")
        bank_name_label_1.grid(row=3, column=0, padx=(10, 10), pady=(10, 10))

        bank_name_entry_1 = Entry(window_2, width=6)
        bank_name_entry_1.insert(0, "Meli")
        bank_name_entry_1.grid(row=3, column=1, padx=(10, 10), pady=(10, 10))

        account_number_label_1 = Label(window_2, text="Account Number")
        account_number_label_1.grid(row=4, column=0, padx=(10, 10), pady=(10, 10))

        account_number_entry_1 = Entry(window_2, width=20)
        account_number_entry_1.grid(row=4, column=1, padx=(10, 10), pady=(10, 10))

        def account_number_button_click():
            account_number_entry_1.delete(0, END)
            number = random.getrandbits(51)
            account_number_entry_1.insert(0, f"{number}")

        account_number_button_1 = Button(window_2, text="Crate a Account Number",
                                         command=account_number_button_click)
        account_number_button_1.grid(row=4, column=2, padx=(10, 10), pady=(10, 10))

        error_label = Label(window_2, text="")
        error_label.grid(row=6, column=2, padx=(10, 10), pady=(10, 10))

        account_balance_label_1 = Label(window_2, text="Account Balance")
        account_balance_label_1.grid(row=5, column=0, padx=(10, 10), pady=(10, 10))

        account_balance_entry_1 = Entry(window_2, width=20)
        account_balance_entry_1.grid(row=5, column=1, padx=(10, 10), pady=(10, 10))

        def save_button_click():
            try:
                first = str(first_name_entry_1.get())
                last = str(last_name_entry_1.get())
                national = int(national_code_entry_1.get())
                bank_name = "Meli"
                account_number = int(account_number_entry_1.get())
                account_balance = float(account_balance_entry_1.get())
            except:
                error_label.config(text=f"First Name = str\nLast Name = str\nNational Code = int\nAccount Number "
                                        f"= int\nAccount Balance = float ", fg="Olive")
            else:
                with sqlite3.connect("BankDB.db") as connection_2:
                    cursor_2 = connection_2.cursor()
                    cursor_2.execute(f"""
                    INSERT INTO Bank (
                                         bank_name,
                                         account_number,
                                         account_balance,
                                         first_name,
                                         last_name,
                                         national_code
                                     )
                                     VALUES (
                                         '{bank_name}',
                                         '{account_number}',
                                         '{account_balance}',
                                         '{first}',
                                         '{last}',
                                         '{national}'
                                     );
                                     """)
                    connection_2.commit()
                    window_2.destroy()
                    create_table_body()

        save_button = Button(window_2, text="Save", command=save_button_click)
        save_button.grid(row=6, column=1, padx=(10, 10), pady=(10, 10))

    create_account_button = Button(window_1, text="Click to Create a Account",
                                   command=create_account_button_click)
    create_account_button.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

    search_entry = Entry(window_1, width=20)
    search_entry.grid(row=0, column=3, padx=(10, 10), pady=(10, 10))

    search_error = Label(window_1, text="")
    search_error.grid(row=0, column=2, padx=(10, 10), pady=(10, 10))

    def search_button_click():
        try:
            search = int(search_entry.get())
        except:
            search_error.config(text="There is no specification with this national code", fg="Maroon")
        else:
            with sqlite3.connect("BankDB.db") as connection_7:
                cursor_7 = connection_7.cursor()
                data_7 = cursor_7.execute("""
                                            SELECT id,
                                                   bank_name,
                                                   account_number,
                                                   account_balance,
                                                   first_name,
                                                   last_name,
                                                   national_code
                                            FROM Bank;
                                             """).fetchall()
                for item_3 in data_7:
                    if search == item_3[6]:
                        search_error.config(text="")
                        window_3 = Tk()
                        window_3.title("Search")
                        row_label_1 = Label(window_3, text="#")
                        row_label_1.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

                        bank_name_label_1 = Label(window_3, text="Bank Name")
                        bank_name_label_1.grid(row=1, column=1, padx=(10, 10), pady=(10, 10))

                        account_number_label_1 = Label(window_3, text="Account Number")
                        account_number_label_1.grid(row=1, column=2, padx=(10, 10), pady=(10, 10))

                        account_balance_label_1 = Label(window_3, text="Account Balance")
                        account_balance_label_1.grid(row=1, column=3, padx=(10, 10), pady=(10, 10))

                        first_name_label_1 = Label(window_3, text="First Name")
                        first_name_label_1.grid(row=1, column=4, padx=(10, 10), pady=(10, 10))

                        last_name_label_1 = Label(window_3, text="Last Name")
                        last_name_label_1.grid(row=1, column=5, padx=(10, 10), pady=(10, 10))

                        national_code_label_1 = Label(window_3, text="National Code")
                        national_code_label_1.grid(row=1, column=6, padx=(10, 10), pady=(10, 10))

                        time_label_1 = Label(window_3, text=f"Searched on this date and time : \n {time.ctime()}",
                                             fg="white",
                                             bg="black")
                        time_label_1.grid(row=3, column=0, padx=(10, 10), pady=(10, 10))

                        with sqlite3.connect("BankDB.db") as connection_5:
                            cursor_5 = connection_5.cursor()
                            data_5 = cursor_5.execute(
                                f"""SELECT * FROM Bank WHERE national_code= {search} """).fetchall()

                            saved_data_1 = []

                            for item_1 in data_5:
                                row_entry = Entry(window_3, width=4)
                                row_entry.insert(0, f"{1}")
                                row_entry.grid(row=2, column=0, padx=(10, 10), pady=(10, 10))
                                saved_data_1.append(row_entry)

                                bank_name_entry = Entry(window_3, width=6)
                                bank_name_entry.insert(0, item_1[1])
                                bank_name_entry.grid(row=2, column=1, padx=(10, 10), pady=(10, 10))
                                saved_data_1.append(bank_name_entry)

                                account_number_entry = Entry(window_3, width=20)
                                account_number_entry.insert(0, item_1[2])
                                account_number_entry.grid(row=2, column=2, padx=(10, 10), pady=(10, 10))
                                saved_data_1.append(account_number_entry)

                                account_balance_entry = Entry(window_3, width=20)
                                account_balance_entry.insert(0, item_1[3])
                                account_balance_entry.grid(row=2, column=3, padx=(10, 10), pady=(10, 10))
                                saved_data_1.append(account_balance_entry)

                                first_name_entry = Entry(window_3, width=20)
                                first_name_entry.insert(0, item_1[4])
                                first_name_entry.grid(row=2, column=4, padx=(10, 10), pady=(10, 10))
                                saved_data_1.append(first_name_entry)

                                last_name_entry = Entry(window_3, width=20)
                                last_name_entry.insert(0, item_1[5])
                                last_name_entry.grid(row=2, column=5, padx=(10, 10), pady=(10, 10))
                                saved_data_1.append(last_name_entry)

                                national_code_entry = Entry(window_3, width=15)
                                national_code_entry.insert(0, item_1[6])
                                national_code_entry.grid(row=2, column=6, padx=(10, 10), pady=(10, 10))
                                saved_data_1.append(national_code_entry)

    search_button = Button(window_1, text="Search", command=search_button_click)
    search_button.grid(row=0, column=4, padx=(10, 10), pady=(10, 10))

    def delete_button_click(id):
        with sqlite3.connect("BankDB.db") as connection_3:
            cursor_3 = connection_3.cursor()
            cursor_3.execute(f"""
                    DELETE FROM Bank
                    WHERE id = {id}""")
        create_table_body()

    saved_data = []

    def create_table_body():
        for j in saved_data:
            j.destroy()
        saved_data.clear()

        with sqlite3.connect("BankDB.db") as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                        SELECT id,
                               bank_name,
                               account_number,
                               account_balance,
                               first_name,
                               last_name,
                               national_code
                          FROM Bank;""").fetchall()
        row = 2
        for i in data:
            row_entry = Entry(window_1, width=4)
            row_entry.insert(0, f"{row - 1}")
            row_entry.grid(row=row, column=0, padx=(10, 10), pady=(10, 10))
            saved_data.append(row_entry)

            bank_name_entry = Entry(window_1, width=6)
            bank_name_entry.insert(0, i[1])
            bank_name_entry.grid(row=row, column=1, padx=(10, 10), pady=(10, 10))
            saved_data.append(bank_name_entry)

            account_number_entry = Entry(window_1, width=20)
            account_number_entry.insert(0, i[2])
            account_number_entry.grid(row=row, column=2, padx=(10, 10), pady=(10, 10))
            saved_data.append(account_number_entry)

            account_balance_entry = Entry(window_1, width=20)
            account_balance_entry.insert(0, i[3])
            account_balance_entry.grid(row=row, column=3, padx=(10, 10), pady=(10, 10))
            saved_data.append(account_balance_entry)

            first_name_entry = Entry(window_1, width=20)
            first_name_entry.insert(0, i[4])
            first_name_entry.grid(row=row, column=4, padx=(10, 10), pady=(10, 10))
            saved_data.append(first_name_entry)

            last_name_entry = Entry(window_1, width=20)
            last_name_entry.insert(0, i[5])
            last_name_entry.grid(row=row, column=5, padx=(10, 10), pady=(10, 10))
            saved_data.append(last_name_entry)

            national_code_entry = Entry(window_1, width=15)
            national_code_entry.insert(0, i[6])
            national_code_entry.grid(row=row, column=6, padx=(10, 10), pady=(10, 10))
            saved_data.append(national_code_entry)

            delete_button = Button(window_1, text="Delete", command=lambda id=i[0]: delete_button_click(id))
            delete_button.grid(row=row, column=7, padx=(10, 10), pady=(10, 10))
            saved_data.append(delete_button)

            row += 1

    create_table_body()


login_button = Button(text="Login", command=login_button_click)
login_button.grid(row=3, column=0, padx=(10, 10), pady=(10, 10))


def sing_in_button_clik():
    window_4 = Tk()
    window_4.title("Confirmation of the bank president")

    username_label_1 = Label(window_4, text="Username of the bank president :")
    username_label_1.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

    username_entry_1 = Entry(window_4, width=30)
    username_entry_1.grid(row=0, column=1, padx=(10, 10), pady=(10, 10))

    password_label_1 = Label(window_4, text="Password of the bank president : ")
    password_label_1.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

    password_entry_1 = Entry(window_4, width=30)
    password_entry_1.grid(row=1, column=1, padx=(10, 10), pady=(10, 10))

    def enter_button_click():
        user = username_entry_1.get()
        password = password_entry_1.get()

        with sqlite3.connect("BankDB.db") as connection_8:
            cursor_8 = connection_8.cursor()
            data_8 = cursor_8.execute("""
                                SELECT id,
                                       username_of_the_bank_president,
                                       password_of_the_bank_president
                                FROM Bank_president;""").fetchall()

            for item_4 in data_8:
                if user == item_4[1] and password == item_4[2]:
                    window_4.destroy()
                    create_window_5()
                else:
                    error_label = Label(window_4, text="Invalid Username or Password", fg="Maroon")
                    error_label.grid(row=2, column=1, padx=(10, 10), pady=(10, 10))

    def show_bank_user_list_button_click():
        user = username_entry_1.get()
        password = password_entry_1.get()

        with sqlite3.connect("BankDB.db") as connection_10:
            cursor_10 = connection_10.cursor()
            data_10 = cursor_10.execute("""
                        SELECT id,
                               username_of_the_bank_president,
                               password_of_the_bank_president
                        FROM Bank_president;""").fetchall()
            for item_5 in data_10:
                if user == item_5[1] and password == item_5[2]:
                    error_label = Label(window_4, text="")
                    error_label.grid(row=2, column=1, padx=(10, 10), pady=(10, 10))
                    create_window_6()
                else:
                    error_label = Label(window_4, text="Invalid Username or Password", fg="Maroon")
                    error_label.grid(row=2, column=1, padx=(10, 10), pady=(10, 10))

    show_bank_user_list_button = Button(window_4, text="Click to show bank user list",
                                        command=show_bank_user_list_button_click)
    show_bank_user_list_button.grid(row=3, column=0, padx=(10, 10), pady=(10, 10))

    enter_button = Button(window_4, text="Enter", command=enter_button_click)
    enter_button.grid(row=3, column=1, padx=(10, 10), pady=(10, 10))

    def create_window_6():
        window_4.destroy()
        window.destroy()
        window_6 = Tk()
        window_6.title("Show bank users")

        row_label = Label(window_6, text="#")
        row_label.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

        username_label_header = Label(window_6, text="Username")
        username_label_header.grid(row=1, column=1, padx=(10, 10), pady=(10, 10))

        password_label_header = Label(window_6, text="Password")
        password_label_header.grid(row=1, column=2, padx=(10, 10), pady=(10, 10))

        def delete_button_click_1(id):
            with sqlite3.connect("BankDB.db") as connection_12:
                cursor_12 = connection_12.cursor()
                cursor_12.execute(f"""
                DELETE FROM Bank_user
                WHERE id = {id}""")
            crate_table_bode_for_window_6()

        save_data_1 = []

        def crate_table_bode_for_window_6():
            for i in save_data_1:
                i.destroy()
            save_data_1.clear()

            with sqlite3.connect("BankDB.db") as connection_11:
                cursor_11 = connection_11.cursor()
                data_11 = cursor_11.execute("""
                                    SELECT id,
                                           username,
                                           password
                                    FROM Bank_user;""").fetchall()
                row = 2
                for item_6 in data_11:
                    row_entry_1 = Entry(window_6, width=4)
                    row_entry_1.insert(0, f"{row - 1}")
                    row_entry_1.grid(row=row, column=0, padx=(10, 10), pady=(10, 10))
                    save_data_1.append(row_entry_1)

                    username_entry_body = Entry(window_6, width=30)
                    username_entry_body.insert(0, f"{item_6[1]}")
                    username_entry_body.grid(row=row, column=1, padx=(10, 10), pady=(10, 10))
                    save_data_1.append(username_entry_body)

                    password_entry_body = Entry(window_6, width=30)
                    password_entry_body.insert(0, f"{item_6[2]}")
                    password_entry_body.grid(row=row, column=2, padx=(10, 10), pady=(10, 10))
                    save_data_1.append(password_entry_body)

                    delete_button_1 = Button(window_6, text="Delete",
                                             command=lambda id=item_6[0]: delete_button_click_1(id))
                    delete_button_1.grid(row=row, column=3, padx=(0, 0), pady=(10, 10))
                    save_data_1.append(delete_button_1)

                    row += 1

        crate_table_bode_for_window_6()


def create_window_5():
    window.destroy()
    window_5 = Tk()
    window_5.title("Add account for bank user")

    username_label_2 = Label(window_5, text="Username :")
    username_label_2.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

    username_entry_2 = Entry(window_5, width=30)
    username_entry_2.grid(row=0, column=1, padx=(10, 10), pady=(10, 10))

    password_label_2 = Label(window_5, text="Password :")
    password_label_2.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

    password_entry_2 = Entry(window_5, width=30)
    password_entry_2.grid(row=1, column=1, padx=(10, 10), pady=(10, 10))

    def save_button_click_2():
        user = username_entry_2.get()
        password = password_entry_2.get()

        with sqlite3.connect("BankDB.db") as connection_9:
            cursor_9 = connection_9.cursor()
            cursor_9.execute(f"""
            INSERT INTO Bank_user (
                          username,
                          password
                          )
                          VALUES (
                              '{user}',
                              '{password}'
                          );
                            """)
            connection_9.commit()
            window_5.destroy()
            window.update()

    save_button_2 = Button(window_5, text="Save", command=save_button_click_2)
    save_button_2.grid(row=2, column=1, padx=(10, 10), pady=(10, 10))


sing_in_button = Button(text="Sing in", command=sing_in_button_clik)
sing_in_button.grid(row=3, column=2, padx=(10, 10), pady=(10, 10))

window.mainloop()
