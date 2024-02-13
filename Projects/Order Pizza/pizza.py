import tkinter as tk

def submit():
    size = size_entry.get().lower()
    peperoni = peperoni_entry.get().lower()
    cheese = cheese_entry.get().lower()
    phone = phone_entry.get()
    counter = 0
    if size == "s":
        counter += 50
    elif size == "m":
        counter += 70
    elif size == "l":
        counter += 100

    if size == "s" and peperoni == "yes":
        counter += 20
    elif size == "m" and peperoni == "yes":
        counter += 30
    elif size == "40" and peperoni == "yes":
        counter += 40

    if size == "s" and peperoni == "yes" and cheese == "yes":
        counter += 30
    elif size == "m" and peperoni == "yes" and cheese == "yes":
        counter += 30
    elif size == "l" and peperoni == "yes" and cheese == "yes":
        counter += 30

    submit_label.config(text=f"Now your Price = {counter}\n your phone number = {phone}")


window = tk.Tk()
window.title("Pizza Golmir")

size_label = tk.Label(text="Please enter the pizza size [ S , M , L]: ")
size_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

size_entry = tk.Entry(width=20)
size_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10))

peperoni_label = tk.Label(text="Do you want a Peperoni [yes or no]? ")
peperoni_label.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

peperoni_entry = tk.Entry(width=20)
peperoni_entry.grid(row=1, column=1, padx=(0, 10), pady=(10, 10))

cheese_label = tk.Label(text="Do you want a Cheese [yes or no]? ")
cheese_label.grid(row=2, column=0, padx=(10, 10), pady=(10, 10))

cheese_entry = tk.Entry(width=20)
cheese_entry.grid(row=2, column=1, padx=(0, 10), pady=(10, 10))

phone_label = tk.Label(text="PLease enter the phone number: ")
phone_label.grid(row=3, column=0, padx=(10, 10), pady=(10, 10))

phone_entry = tk.Entry(width=20)
phone_entry.grid(row=3, column=1, padx=(0, 10), pady=(10, 10))

submit_label = tk.Label(text="Empty")
submit_label.grid(row=4, column=1, padx=(10, 10), pady=(10, 10))

submit_button = tk.Button(text="Click To Submit", bg="yellow", command=submit)
submit_button.grid(row=5, column=1, padx=(10, 10), pady=(10, 10))

window.mainloop()
