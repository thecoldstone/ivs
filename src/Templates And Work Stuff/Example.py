#!/usr/bin/env python
# -*- coding: utf-8 -*
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sys
from src.Math import Math

import math

#calcInstance = Calc()

gui = Tk()
gui.title("Calculator")
gui.configure(background="red")
gui.geometry("583x227")

bttn_list = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "/",
    "√x", "xⁿ", "0", "=",
    "sin", "cos", ".", "n!",
    "(", ")", "п", "Clean",
    "Exit", "*",

]

calc_entry = Entry(gui, width=103)
calc_entry.grid(row=0, column=0, columnspan=50)

def calc(key):
    num1 = ''
    num2 = ''
    operation = ''

    if  key != "Exit":
            if (num1 == ''):
                if key.isdigit():
                    num1 = str(calc_entry.get())
                    calc_entry.insert(END, num1)

            if (num1 != ''):
                if key == "+":
                    operation = operation + key
                elif key == "-":
                    operation = operation + key
            if (num2 == ''):

                if key.isdigit():
                    num2 = num2 + key

            if key == "=":
                if operation == "+":
                    result = Math.Add(num1, num2)
                    #calc_entry.insert(END, str(num1) + str(num2))
                    calc_entry.insert(END, int(result))

            if key == "Clean":
                calc_entry.delete(0, END)
            else :
                calc_entry.delete(0, END)
                calc_entry.insert(END, key)

    if key == "Exit":
        gui.after(1, gui.destroy)
        sys.exit()

for i in bttn_list:
    rel = ""
    cmd = lambda x=i:calc(x)  # The statement creates an anonymous function with the lambda keyword.
    # The function multiplies two values. The x is a parameter that is passed to the lambda function.
    # The parameter is followed by a colon character.
    # The code next to the colon is the expression that is executed when the lambda function is called.
    # The lambda function is assigned to the z variable.
    # z = lambda x: x * y

    if i == '7':
        #calcInstance.insertNumber()
        Button(gui, text=i, command=cmd, fg='black', bg='light blue', width=19).grid(row=1, column=0, columnspan=1)
    if i == '8':
        Button(gui, text=i, command=cmd, fg='black', bg='white', width=19).grid(row=1, column=1, columnspan=1)
    if i == '9':
        Button(gui, text=i, command=cmd, fg='black', bg='white', width=19).grid(row=1, column=2, columnspan=1)
    if i == '/':
        Button(gui, text=i, command=cmd, fg='black', bg='white', width=19).grid(row=1, column=3, columnspan=1)
    if i == '4':
        Button(gui, text=i, command=cmd, fg='black', bg='red', width=19).grid(row=2, column=0, columnspan=1)
    if i == '5':
        Button(gui, text=i, command=cmd, fg='black', bg='white', width=19).grid(row=2, column=1, columnspan=1)
    if i == '6':
        Button(gui, text=i, command=cmd, fg='black', bg='white', width=19).grid(row=2, column=2, columnspan=1)
    if i == '*':
        Button(gui, text=i, command=cmd, fg='black', bg='white', width=19).grid(row=2, column=3,columnspan=1)  # by the defualt columnspn is
    if i == '1':
        Button(gui, text=i, command=cmd, fg='black', bg='white', width=19).grid(row=3, column=0, columnspan=1)
        # ttk.Button(gui, text=i, command=cmd, style="TButton", width=19).grid(row=3, column=0, columnspan=1)
    if i == '2':
        Button(gui, text=i, command=cmd, fg='black', bg='white', width=19).grid(row=3, column=1, columnspan=1)
    if i == '3':
        Button(gui, text=i, command=cmd, fg='black', bg='white', width=19).grid(row=3, column=2, columnspan=1)
    if i == '-':
        Button(gui, text=i, command=cmd, fg='black', bg='white', width=19).grid(row=3, column=3, columnspan=1)
    if i == '0':
        Button(gui, text=i, command=cmd, fg='black', bg='white', width=40).grid(row=4, column=0, columnspan=2)
    if i == 'xⁿ':
        Button(gui, text=i, command=cmd, fg='black', bg='white', width=19).grid(row=5, column=3, columnspan=1)
    if i == '.':
        Button(gui, text=i, command=cmd, fg='black', bg='white', width=19).grid(row=4, column=2, columnspan=1)
    if i == '+':
        Button(gui, text=i, command=cmd, fg='black', bg='white', width=19).grid(row=4, column=3, columnspan=1)
    if i == '(':  # http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-style-layer.html
        Button(gui, text=i, command=cmd, fg='black', bg='white', width=19).grid(row=5, column=0, columnspan=1)
    if i == ')':
        Button(gui, text=i, command=cmd, fg='black', bg='white', width=19).grid(row=5, column=1, columnspan=1)
    if i == 'п':
        Button(gui, text=i, command=cmd, fg='black', bg='white', width=19).grid(row=5, column=2, columnspan=1)
    if i == 'sin':
        Button(gui, text=i, command=cmd, fg='black', bg='white', width=19).grid(row=6, column=0, columnspan=1)
    if i == 'cos':  # http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-style-layer.html
        Button(gui, text=i, command=cmd, fg='black', bg='white', width=19).grid(row=6, column=1, columnspan=1)
    if i == '√x':
        Button(gui, text=i, command=cmd, fg='black', bg='white', width=19).grid(row=6, column=2, columnspan=1)
    if i == 'n!':
        Button(gui, text=i, command=cmd, fg='black', bg='white', width=19).grid(row=6, column=3, columnspan=1)
    if i == 'Exit':
        Button(gui, text=i, command=cmd, fg='black', bg='white', width=82).grid(row=8, column=0, columnspan=4)
    if i == 'Clean':
        Button(gui, text=i, command=cmd, fg='black', bg='white', width=40).grid(row=7, column=0, columnspan=2)
    if i == '=':
        Button(gui, text=i, command=cmd, fg='black', bg='white', width=40).grid(row=7, column=2, columnspan=2)
# логика калькулятора



gui.mainloop()