# calculator
#### *this project is a calculator and has three inputs.*

*first input is for the number , second input for operation and third input for the number.*

*the operations that this calculator performans is : addition , subtarction , multiplication , division , power and 
logarithm.*

+ operation are as fllows :

```python
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
            subtraction = number1 - number2
            generate_label.config(text=f"{subtraction}")

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
```