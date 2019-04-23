#!/usr/bin/python
# -*- coding: utf-8 -*

'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

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

        if key == "⌫":
            equation = equation[:-1]
            entry_input.delete(len(entry_input.get()) - 1, tk.END)
        elif key == "Clean":
            del memory[0:len(memory)]
            equation = ""
            operation = ""
            entry_input.delete(0, END)
        #elif key == "xⁿ":
            #entry_input.insert(INSERT, "**")
        elif key == "√x":
            entry_input.insert(END, "=" + str(math_api.sqrt(Decimal(entry_input.get()))))
        elif key == "+" or key == "-" or key == "*" or key == "÷" or key == "ABS" or key == "n!" or key == "xⁿ":
            operation = ""
            operation = operation + key
            memory.append(equation)
            equation = ""
            entry_input.delete(0, END)

            #if operation == "n!":
             #   memory[0] = entry_input.insert(END, calculate(Decimal(memory[0]), operation))
              #  entry_input.insert(END, str(memory[0]))

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
        if operator == "xⁿ":
            return math_api.power(eq, Decimal(equation))


    root = create_root()
    entry_input = create_entry(root)
    create_buttons(root, process_key_press)

    memory = []
    equation = ""
    operation = ""

    root.mainloop()
