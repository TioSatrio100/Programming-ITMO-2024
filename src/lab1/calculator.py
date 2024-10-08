"""
Module for performing basic calculator operations.
This module provides functions to add, subtract,
multiply, and divide two numbers.
"""

import tkinter as tk


# Make function
def plus():
    """
    Add two numbers and display the result.
    """
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 + num2
    label_result.config(text="result: " + str(result))


def minus():
    """
    Subtract two numbers and display the result.
    """
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 - num2
    label_result.config(text="result: " + str(result))


def times():
    """
    Multiply two numbers and display the result.
    """
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 * num2
    label_result.config(text="result: " + str(result))


def divide():
    """
    Divide two numbers and display the result.
    """
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 / num2
    label_result.config(text="result: " + str(result))


# Make GUI Window
window = tk.Tk()
window.title("Simple Calculator")

# Make interface
entry_num1 = tk.Entry(window)
entry_num1.pack()

entry_num2 = tk.Entry(window)
entry_num2.pack()

button_plus = tk.Button(window, text="+", command=plus)
button_plus.pack()

button_minus = tk.Button(window, text="-", command=minus)
button_minus.pack()

button_times = tk.Button(window, text="*", command=times)
button_times.pack()

button_divide = tk.Button(window, text="/", command=divide)
button_divide.pack()

label_result = tk.Label(window, text="result: ")
label_result.pack()

# Show window GUI
window.mainloop()
