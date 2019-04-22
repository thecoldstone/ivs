#!/usr/bin/python
#!/usr/bin/env python
# -*- coding: utf-8 -*
import tkinter as tk    # py3
from src.colorsforcalc import *
from tkinter import *
from tkinter import  font
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from src.Math import *
import sys
import tkinter
from tkinter import font
import tkinter.font as ass


class Example(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        f1 = GradientFrame(self, borderwidth=1, relief="sunken")
        f1.pack(side="top", fill="both", expand=True)


class GradientFrame(tk.Canvas):
    '''A gradient frame which uses a canvas to draw the background'''
    def __init__(self, parent, **kwargs):
        colors = PickColors()
        tk.Canvas.__init__(self, parent, **kwargs)
        self._color1 = colors[0]
        self._color2 = colors[1]
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event=None):
        '''Draw the gradient'''
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1,g1,b1) = self.winfo_rgb(self._color1)
        (r2,g2,b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
            self.create_line(i,0,i,2000, tags=("gradient",), fill=color)
        self.lower("gradient")

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.title("Calculator")
    root.geometry("600x600")

    helv40 = font.Font(family='Arial', size=16, weight='bold')
    calc_entry = Entry(root, bg="white", font="Arial")
    calc_entry.place(relx=0.01, rely=0.01,relheight=0.1, relwidth=0.98)
   # Entry.font(family='Arial', size=16, weight='bold')


    bttn_list = [
        "7", "8", "9", "+",
        "4", "5", "6", "-",
        "1", "2", "3", "÷",
        "√x", "xⁿ", "0", "=",
         ",", "n!","(", ")", "⌫",
        "ABS", "Clean","Exit", "*",
    ]

    memory = []
    equation = ''
    operation = ''

    for i in bttn_list:
        cmd = lambda x=i:show(x)
        if i == '0':
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.0, rely=0.895,relwidth=0.47,relheight=0.1)
        if i == ',':
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.480, rely=0.895, relwidth=0.23, relheight=0.1)
        if i == '1':
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.0, rely=0.790,  relwidth=0.23, relheight=0.1)
        if i == '2':
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.240,rely=0.790,  relwidth=0.23, relheight=0.1)
        if i == '3':
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.480,rely=0.790, relwidth=0.23, relheight=0.1)
        if i == '4':
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.0,rely=0.685, relwidth=0.23, relheight=0.1)
        if i == '5':
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.240,rely=0.685, relwidth=0.23, relheight=0.1)
        if i == '6':
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.480,rely=0.685,relwidth=0.23, relheight=0.1)
        if i == '7':
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.0,rely=0.580,relwidth=0.23, relheight=0.1)
        if i == '8':
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.240,rely=0.580, relwidth=0.23, relheight=0.1)
        if i == '9':
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.480,rely=0.580, relwidth=0.23, relheight=0.1)
        if i == '=':
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.715,rely=0.840, relwidth=0.275, relheight=0.153)
        if i == '+':
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.715,rely=0.685,relwidth=0.275, relheight=0.153)
        if i == '*':
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.715,rely=0.530,relwidth=0.275, relheight=0.153)
        if i == '÷':
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.715,rely=0.375,relwidth=0.275, relheight=0.153)
        if i == '-':
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.715, rely=0.220,relwidth=0.275,relheight=0.153)
        if i == "√x":
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.0, rely=0.475,relwidth=0.23,relheight=0.1)
        if i ==  "xⁿ":
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.240, rely=0.475,relwidth=0.23,relheight=0.1)
        if i == "n!":
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.480,rely=0.475,relwidth=0.23, relheight=0.1)
        if i == "(":
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.0, rely=0.370,relwidth=0.23, relheight=0.1)
        if i == "ABS":
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.240, rely=0.370,relwidth=0.23, relheight=0.1)
        if i == ")":
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.480, rely=0.370,relwidth=0.23, relheight=0.1)
        if i == "Clean":
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.00, rely=0.220,relwidth=0.47, relheight=0.145)
        if i == "⌫":
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.480, rely=0.220,relwidth=0.23, relheight=0.145)

    def show(key):
        global memory
        global equation
        global operation

        if key.isdigit():
            equation = equation + key
            calc_entry.insert(END, key)

        # очищение поля ввода
        if key == "⌫":
            equation = equation[:-1]
            calc_entry.delete(len(calc_entry.get())-1, tk.END)
        elif key == 'Clean':
            del memory[0:len(memory)]
            equation = ''
            operation = ''
            calc_entry.delete(0, END)
        elif key == "xⁿ":
            calc_entry.insert(INSERT, "**")
        elif key == ",":
            calc_entry.insert(END, ",")
        elif key == "√x":
            calc_entry.insert(END, "=" + str(math.sqrt(int(calc_entry.get()))))
        elif key == "+" or key == "-" or key == "*" or key =="÷" or key == "ABS" or key == "n!":
            operation = ''
            operation = operation + key
            memory.append(equation)
            equation = ''
            calc_entry.delete(0, END)
        elif key == "=":
            calc_entry.delete(0, END)
            memory[0] = (calc(int(memory[0]), operation))
            calc_entry.insert(END, str(memory[0]))

    def calc(eq, ops):

        if ops == "-":
            return Math.Sub(eq, int(equation))
        if ops == "+":
            return Math.Add(eq, int(equation))
        if ops == "*":
            return Math.Multiply(eq, int(equation))
        if ops == "÷":
            return Math.Divison(eq, int(equation))
        if ops == "ABS":
            return Math.Abs(eq)
        if ops == "n!":
            return Math.Factorial(eq)



    root.mainloop()