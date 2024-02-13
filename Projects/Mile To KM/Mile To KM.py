import tkinter

window = tkinter.Tk()
window.title("Mile To KM")

mile_label = tkinter.Label(text="Mile:")
mile_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

mile_entry = tkinter.Entry(width=20)
mile_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10))

km_label = tkinter.Label(text="Empty")
km_label.grid(row=1, column=1, padx=(0, 10))


def calculate_button_clicked():
    try:
        mile = float(mile_entry.get())
        km = mile * 1.6
        km_label.config(text=f"Is Equal To {km} KM")
    except:
        km_label.config(text=f"Please Enter The Number!")


calculate_button = tkinter.Button(text="Calculate", bg="yellow", command=calculate_button_clicked)
calculate_button.grid(row=2, column=1, padx=(0, 10), pady=(10, 0))

window.mainloop()
