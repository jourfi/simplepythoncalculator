import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")
window.configure(background='black')  # Set the background color to black

# Create an entry widget to display the numbers and results
entry = tk.Entry(window, width=25, font=("Arial", 12))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entry.configure(background='white')  # Set the background color of the entry widget to white

button_clear = tk.Button(window, text='C', font=("Arial", 12), width=5, command=clear, bg='red', fg='white')  # Set the button color to red and the text color to white
button_clear.grid(row=4, column=1, padx=5, pady=5)

# Create number buttons
for i in range(9):
    button = tk.Button(window, text=str(i+1), font=("Arial", 12), width=5, command=lambda num=i+1: button_click(num))
    button.grid(row=i//3+1, column=i%3, padx=5, pady=5)
    button.configure(bg='black', fg='white')  # Set the background color of number buttons to black and the text color to white

# Create operator buttons
operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    button = tk.Button(window, text=operator, font=("Arial", 12), width=5, command=lambda op=operator: button_click(op))
    button.grid(row=i+1, column=3, padx=5, pady=5)
    button.configure(bg='black', fg='white')  # Set the background color of operator buttons to black and the text color to white

# Create other buttons
button_zero = tk.Button(window, text='0', font=("Arial", 12), width=5, command=lambda: button_click(0))
button_zero.grid(row=4, column=0, padx=5, pady=5)
button_zero.configure(bg='black', fg='white')  # Set the background color of the '0' button to black and the text color to white

button_equal = tk.Button(window, text='=', font=("Arial", 12), width=5, command=calculate)
button_equal.grid(row=4, column=2, padx=5, pady=5)
button_equal.configure(bg='black', fg='white')  # Set the background color of the '=' button to black and the text color to white

button_dot = tk.Button(window, text='.', font=("Arial", 12), width=5, command=lambda: button_click('.'))
button_dot.grid(row=5, column=0, padx=5, pady=5)
button_dot.configure(bg='black', fg='white')  # Set the background color of the '.' button to black and the text color to white

# Run the main loop
window.mainloop()
