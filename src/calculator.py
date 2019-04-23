#!/usr/bin/python
# -*- coding: utf-8 -*
import tkinter as tk  # py3
from decimal import *
from tkinter import *

import src.staff.math_api as math_api
from src.staff.buttons import create_buttons
from src.staff.entry_input import create_entry
from src.staff.root import create_root

if __name__ == "__main__":

    def process_key_press(key):
        global memory
        global equation
        global operation

        if key.isdigit() or key == ".":
            equation += key
            entry_input.insert(END, key)

        # очищение поля ввода
        if key == "⌫":
            equation = equation[:-1]
            entry_input.delete(len(entry_input.get()) - 1, tk.END)
        elif key == "Clean":
            del memory[0:len(memory)]
            equation = ""
            operation = ""
            entry_input.delete(0, END)
        elif key == "xⁿ":
            entry_input.insert(INSERT, "**")
        elif key == "√x":
            entry_input.insert(END, "=" + str(math_api.sqrt(Decimal(entry_input.get()))))
        elif key == "+" or key == "-" or key == "*" or key == "÷" or key == "ABS" or key == "n!":
            operation = ""
            operation = operation + key
            memory.append(equation)
            equation = ""
            entry_input.delete(0, END)
        elif key == "=":
            entry_input.delete(0, END)
            memory[0] = calculate(Decimal(memory[0]), operation)
            entry_input.insert(END, str(memory[0]))


    def calculate(eq, operator):
        if operator == "-":
            return math_api.sub(eq, Decimal(equation))
        if operator == "+":
            return math_api.add(eq, Decimal(equation))
        if operator == "*":
            return math_api.multiply(eq, Decimal(equation))
        if operator == "÷":
            return math_api.division(eq, Decimal(equation))
        if operator == "ABS":
            return math_api.absolute(eq)
        if operator == "n!":
            return math_api.factorial(eq)


    root = create_root()
    entry_input = create_entry(root)
    create_buttons(root, process_key_press)

    memory = []
    equation = ""
    operation = ""

    root.mainloop()
