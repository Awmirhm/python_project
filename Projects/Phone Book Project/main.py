import tkinter as tk
import Phone_Book

file = open("phonebook.txt", mode="r")

phonebook = Phone_Book.PhoneBook()

window = tk.Tk()
window.title("Phone Book")


def add_new_contact_button_click():
    window_1 = tk.Tk()
    window_1.title("Crate a New Contact")

    name_label = tk.Label(window_1, text="Name : ")
    name_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

    name_entry = tk.Entry(window_1, width=30)
    name_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10))

    phone_label = tk.Label(window_1, text="Phone Number : ")
    phone_label.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

    phone_entry = tk.Entry(window_1, width=30)
    phone_entry.grid(row=1, column=1, padx=(0, 10), pady=(10, 10))

    def save_button_click():
        name = name_entry.get()
        phone = phone_entry.get()
        phonebook.add_contact(name, phone)

        with open("phonebook.txt", mode="a") as file:
            file.write(f"\n{name},{phone}")

        window_1.destroy()

        crate_table_body()

    save_button = tk.Button(window_1, text="Click to Save", command=save_button_click)
    save_button.grid(row=2, column=1, padx=(10, 0), pady=(10, 10))


add_new_contact_button = tk.Button(text="Click to Crate a New Contact", command=add_new_contact_button_click)
add_new_contact_button.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

search_entry = tk.Entry(width=30)
search_entry.grid(row=0, column=1, padx=(0, 0), pady=(10, 10))


def search_button_click():
    search = search_entry.get()
    phonebook.search_contact(search)

    crate_table_body()


search_button = tk.Button(text="Search", command=search_button_click)
search_button.grid(row=0, column=2, padx=(10, 10), pady=(10, 10))


def crate_table_head():
    row_label = tk.Label(text="No")
    row_label.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

    name_label = tk.Label(text="Name")
    name_label.grid(row=1, column=1, padx=(10, 10), pady=(10, 10))

    phone_label = tk.Label(text="Phone Number")
    phone_label.grid(row=1, column=2, padx=(10, 10), pady=(10, 10))


crate_table_head()

entry_list = []


def delete_button_click(name, number):
    phonebook.delete_contact(name, number)
    content = ""
    for i in phonebook.contact_list:
        content += f"{i.full_name},{i.phone_number}"
        with open("phonebook.txt", mode="w") as file_2:
            file_2.write(content)

    crate_table_body()


def crate_table_body():
    for x in entry_list:
        x.destroy()

    entry_list.clear()

    row = 1
    for i in phonebook.show_contact_list:
        row_entry = tk.Entry(width=4)
        row_entry.insert(0, row)
        row_entry.grid(row=1 + row, column=0)
        entry_list.append(row_entry)

        name_entry = tk.Entry(width=30)
        name_entry.insert(0, i.full_name)
        name_entry.grid(row=1 + row, column=1)
        entry_list.append(name_entry)

        phone_entry = tk.Entry(width=12)
        phone_entry.insert(0, i.phone_number)
        phone_entry.grid(row=1 + row, column=2)
        entry_list.append(phone_entry)

        delete_button = tk.Button(text="Delete", command=lambda name=i.full_name, phone=i.phone_number:
        delete_button_click(name, phone))
        delete_button.grid(row=1 + row, column=3)
        entry_list.append(delete_button)

        row += 1


with open("phonebook.txt", mode="r") as file_1:
    for i in file_1.readlines():
        date = i.split(",")
        name = date[0]
        phone = date[1]
        phonebook.add_contact(name, phone)

crate_table_body()

window.mainloop()
