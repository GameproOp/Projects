import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operator_var.get()
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"
        
        result_label.config(text="Result: " + str(result))
        
    except ValueError:
        result_label.config(text="Invalid input!")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create entry fields
entry1 = tk.Entry(window, width=10)
entry1.pack(pady=10)

entry2 = tk.Entry(window, width=10)
entry2.pack(pady=10)

# Create operator selection
operator_var = tk.StringVar(window)
operator_var.set("+")  # Default operator

operator_dropdown = tk.OptionMenu(window, operator_var, "+", "-", "*", "/")
operator_dropdown.pack(pady=10)

# Create calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack(pady=10)

# Create result label
result_label = tk.Label(window, text="Result: ")
result_label.pack(pady=10)

# Start the main loop
window.mainloop()
