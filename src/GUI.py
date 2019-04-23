#!/usr/bin/python
#!/usr/bin/env python
# -*- coding: utf-8 -*
import tkinter as tk    # py3
from src.staff.pick_colors import *
from tkinter import *
from tkinter import  font
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import math
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
        colors = pick_colors()
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
        "п", "Clean","Exit", "*",
    ]
    '''
    B = tk.Button(text="0")          #,bg=PickColor())
    B['font'] = font.Font(family='Arial', size=16, weight='bold')
    B.pack()
    B.place(height=50, width=300, relx=0.235, rely=0.96, anchor=CENTER)

    B = tk.Button(text=",")
    B['font'] = font.Font(family='Arial', size=16, weight='bold')
    B.pack()
    B.place(height=50, width=150, relx=0.62, rely=0.96, anchor=CENTER)

    B = tk.Button(text="1")
    B['font'] = helv40
    B.pack()
    B.place(height=50, width=150,relx=0.1, rely=0.87,anchor=CENTER)

    B = tk.Button(text="2")
    B['font'] = helv40
    B.pack()
    B.place(height=50, width=150, relx=0.36, rely=0.87, anchor=CENTER)

    B = tk.Button(text="3")
    B['font'] = helv40
    B.pack()
    B.place(height=50, width=150, relx=0.62, rely=0.87, anchor=CENTER)

    B = tk.Button(text="4")
    B['font'] = helv40
    B.pack()
    B.place(height=50, width=150, relx=0.1, rely=0.78, anchor=CENTER)

    B = tk.Button(text="5")
    B['font'] = helv40
    B.pack()
    B.place(height=50, width=150, relx=0.36, rely=0.78, anchor=CENTER)

    B = tk.Button(text="6")
    B['font'] = helv40
    B.pack()
    B.place(height=50, width=150, relx=0.62, rely=0.78, anchor=CENTER)

    B = tk.Button(text="7")
    B['font'] = helv40
    B.pack()
    B.place(height=50, width=150, relx=0.1, rely=0.69, anchor=CENTER)

    B = tk.Button(text="8")
    B['font'] = helv40
    B.pack()
    B.place(height=50, width=150, relx=0.36, rely=0.69, anchor=CENTER)

    B = tk.Button(text="9")
    B['font'] = helv40
    B.pack()
    B.place(height=50, width=150, relx=0.62, rely=0.69, anchor=CENTER)

    B = tk.Button(text="+")
    B['font'] = font.Font(family='Arial', size=20, weight='bold')
    B.pack()
    B.place(height=75, width=144, relx=0.87, rely=0.94, anchor=CENTER)

    B = tk.Button(text="–")
    B['font'] = font.Font(family='Arial', size=20, weight='bold')
    B.pack()
    B.place(height=75, width=144, relx=0.87, rely=0.80, anchor=CENTER)

    B = tk.Button(text="*")
    B['font'] = font.Font(family='Arial', size=24, weight='bold')
    B.pack()
    B.place(height=75, width=144, relx=0.87, rely=0.66, anchor=CENTER)

    B = tk.Button(text="÷")
    B['font'] = font.Font(family='Arial', size=20, weight='bold')
    B.pack()
    B.place(height=75, width=144, relx=0.87, rely=0.52, anchor=CENTER)
    '''

    for i in bttn_list:
        cmd = lambda x=i:calc(x)
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
        if i =="√x":
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.0, rely=0.475,relwidth=0.23,relheight=0.1)
        if i ==  "xⁿ":
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.240, rely=0.475,relwidth=0.23,relheight=0.1)
        if i == "n!":
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.480,rely=0.475,relwidth=0.23, relheight=0.1)
        if i == "(":
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.0, rely=0.370,relwidth=0.23, relheight=0.1)
        if i == "п":
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.240, rely=0.370,relwidth=0.23, relheight=0.1)
        if i == ")":
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.480, rely=0.370,relwidth=0.23, relheight=0.1)
        if i == "Clean":
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.00, rely=0.220,relwidth=0.47, relheight=0.145)
        if i == "⌫":
            B = tk.Button(root, bg="white", text=i, font='Arial', command=cmd, width=1).place(relx=0.480, rely=0.220,relwidth=0.23, relheight=0.145)

    def calc(key):
        # очищение поля ввода
        if key == "⌫":
            calc_entry.delete(len(calc_entry.get())-1, tk.END)
        elif key == 'Clean':
            calc_entry.delete(0, END)
        elif key == "п":
            calc_entry.insert(END, math.pi)
        elif key == "Exit":
            root.aftesr(1, root.destroy)
            sys.exit()
        elif key == "12":
            calc_entry.insert(END, "1")
        elif key == "xⁿ":
            calc_entry.insert(INSERT, "**")
        elif key == "sin":
            calc_entry.insert(END, "=" + str(math.sin(int(calc_entry.get()))))
        elif key == "cos":
            calc_entry.insert(END, "=" + str(math.cos(int(calc_entry.get()))))
        elif key == "1":
            calc_entry.insert(END, "1")
        elif key == ")":
            calc_entry.insert(END, ")")
        elif key == "n!":
            calc_entry.insert(END, "=" + str(math.factorial(int(calc_entry.get()))))
        elif key == "√x":
            calc_entry.insert(END, "=" + str(math.sqrt(int(calc_entry.get()))))
        else:
            if "=" in calc_entry.get():
                calc_entry.delete(0, END)
            calc_entry.insert(END, key)


    root.mainloop()