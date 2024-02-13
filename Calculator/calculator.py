import math
import tkinter as tk

window = tk.Tk()
window.title("Calculator")

number_1_label = tk.Label(text="Number 1: ")
number_1_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

number_1_entry = tk.Entry(width=20)
number_1_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10))

operation_label = tk.Label(text="Operation: ")
operation_label.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

operation_entry = tk.Entry(width=20)
operation_entry.grid(row=1, column=1, padx=(0, 10), pady=(10, 10))

number_2_label = tk.Label(text="Number 2: ")
number_2_label.grid(row=2, column=0, padx=(10, 10), pady=(10, 10))

number_2_entry = tk.Entry(width=20)
number_2_entry.grid(row=2, column=1, padx=(0, 10), pady=(10, 10))


def calculate():
    operation = operation_entry.get()
    try:
        number1 = float(number_1_entry.get())
        number2 = float(number_2_entry.get())
    except:
        generate_label.config(text="Please entre the number!!")

    else:

        if operation == "+":
            addition = number1 + number2
            generate_label.config(text=f"{addition}")

        elif operation == "-":
            subtarction = number1 - number2
            generate_label.config(text=f"{subtarction}")

        elif operation == "*":
            multiplication = number1 * number2
            generate_label.config(text=f"{multiplication}")

        elif operation == "/":
            try:
                division = number1 / number2
            except:
                generate_label.config(text=f"Error")
            else:
                generate_label.config(text=f"{division}")

        elif operation == "**":
            power = math.pow(number1, number2)
            generate_label.config(text=f"{power}")

        elif operation == "log":
            try:
                logarithm = math.log(number1, number2)
            except:
                generate_label.config(text=f"Error")
            else:
                generate_label.config(text=f"{logarithm}")


generate_label = tk.Label(text="Empty")
generate_label.grid(row=3, column=1, padx=(0, 20), pady=(10, 10))

generate_button = tk.Button(text="Generate", bg="yellow", command=calculate)
generate_button.grid(row=4, column=1, padx=(0, 20), pady=(10, 10))

window.mainloop()
