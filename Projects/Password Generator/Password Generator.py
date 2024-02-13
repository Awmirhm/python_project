import tkinter
import random


def crate_password():
    password_entry.delete(0,tkinter.END)
    list_1 = ""
    list_2 = ""
    website = website_entry.get()
    username = email_username_entry.get()
    list_1 = website + list_1
    list_1 = username + list_1
    for i in range(8):
        a = random.choice(list_1)
        list_2 = a + list_2

    password_entry.insert(0,list_2)


window = tkinter.Tk()
window.title("information")

website_label = tkinter.Label(text="Website:")
website_label.grid(row=0, column=0, padx=(10, 0), pady=(10, 10))

website_entry = tkinter.Entry(width=40)
website_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10))

email_username_label = tkinter.Label(text="Email/Username:")
email_username_label.grid(row=1, column=0, padx=(10, 0), pady=(0, 0))

email_username_entry = tkinter.Entry(width=40)
email_username_entry.grid(row=1, column=1, padx=(0, 10), pady=(10, 10))

password_label = tkinter.Label(text="Password:")
password_label.grid(row=2, column=0, padx=(10, 0), pady=(10, 10))

password_entry=tkinter.Entry(width=20)
password_entry.grid(row=2, column=1, padx=(0, 130), pady=(10, 10))


generate_password = tkinter.Button(text="Generate Password", bg="yellow", command=crate_password)
generate_password.grid(row=2, column=1, padx=(180, 60), pady=(10, 10))

window.mainloop()
