#calculator app
import tkinter as tk
from tkinter import messagebox

# Function to evaluate the expression and display the result
def calculate():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Function to add a character to the entry widget
def add_to_expression(char):
    entry.insert(tk.END, char)

# Function to clear the entry widget
def clear():
    entry.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")

# Set window size
root.geometry('450x600')

# Entry widget to display the expression and results
entry = tk.Entry(root, font=('Arial', 24), width=15, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=(20, 10))

# Buttons for digits and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create and position the buttons
for (text, row, column) in buttons:
    button = tk.Button(root, text=text, font=('Arial', 18), padx=20, pady=20, command=lambda t=text: add_to_expression(t))
    button.grid(row=row, column=column, padx=10, pady=10)

# Clear button
clear_button = tk.Button(root, text='C', font=('Arial', 18), padx=20, pady=20, command=clear)
clear_button.grid(row=5, column=0, columnspan=3, padx=10, pady=(0, 20))

# Equal button
equal_button = tk.Button(root, text='=', font=('Arial', 18), padx=20, pady=20, command=calculate)
equal_button.grid(row=5, column=3, padx=10, pady=(0, 20))

# Run the main loop
root.mainloop()
