import tkinter as tk

window = tk.Tk()
window.title("Login Page")

username_label = tk.Label(text="Username : ")
username_label.grid(row=0, column=0, padx=(20, 20), pady=(10, 10))

username_entry = tk.Entry(width=30, bg="white", fg="red")
username_entry.grid(row=0, column=1, padx=(0, 20), pady=(10, 10))

password_label = tk.Label(text="Password : ")
password_label.grid(row=1, column=0, padx=(20, 20), pady=(10, 10))

password_entry = tk.Entry(width=30, bg="white", fg='red')
password_entry.grid(row=1, column=1, padx=(0, 20), pady=(10, 10))

showlist = tk.Label(text="Empty")
showlist.grid(row=2, column=1, padx=(0, 20), pady=(10, 10))

showlist_1 = tk.Label(text=" ")
showlist_1.grid(row=0, column=4, padx=(0, 20), pady=(10, 10))

showlist_2 = tk.Label(text=" ")
showlist_2.grid(row=1, column=4, padx=(0, 20), pady=(10, 10))

showlist_3 = tk.Label(text=" ")
showlist_3.grid(row=0, column=5, padx=(0, 20), pady=(10, 10))

showlist_4 = tk.Label(text=" ")
showlist_4.grid(row=1, column=5 , padx=(0, 20), pady=(10, 10))

showlist_5 = tk.Label(text=" ")
showlist_5.grid(row=0, column=6, padx=(0, 20), pady=(10, 10))

li_1 = [
    {
        "first name": "hfjknio",
        "last name": "popjbk"
    },
    {
        "first name": "lkmjn",
        "last name": "bhjjk"
    },
    {
        "first name": "jkmlko",
        "last name": "kopkmmm"
    },
    {
        "first name": "nnjxdc",
        "last name": "wesdcv"
    },
    {
        "first name": "xcbvuyugu",
        "last name": "lmkjnmkh"
    }
]


def click_for_show():
    global li_1
    username = username_entry.get()
    password = password_entry.get()
    if username == "Admin" and password == "1234":
        showlist.config(text=f"Wellcome {username} ")
        showlist_1.config(text=f"1- First name = {li_1[0]["first name"]} , Last name = {li_1[0]["last name"]}")
        showlist_2.config(text=f"2- First name = {li_1[1]["first name"]} , Last name = {li_1[1]["last name"]}")
        showlist_3.config(text=f"3- First name = {li_1[2]["first name"]} , Last name = {li_1[2]["last name"]}")
        showlist_4.config(text=f"4- First name = {li_1[3]["first name"]} , Last name = {li_1[3]["last name"]}")
        showlist_5.config(text=f"5- First name = {li_1[4]["first name"]} , Last name = {li_1[4]["last name"]}")
    else:
        showlist.config(text="Invalid username or password")


showlist_button = tk.Button(text="Click to show list", bg="yellow", command=click_for_show)
showlist_button.grid(row=3, column=1, padx=(0, 20), pady=(10, 10))

window.mainloop()
