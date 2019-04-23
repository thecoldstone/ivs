import tkinter as tk  # py3
from tkinter import font


def create_buttons(root, callback):
    for button in [
        "7", "8", "9", "+",
        "4", "5", "6", "-",
        "1", "2", "3", "÷",
        "√x", "xⁿ", "0", "=",
        ".", "n!", "(", ")", "⌫",
        "ABS", "Clean", "Exit", "*",
    ]:
        render_button(button, lambda key=button: callback(key), root)


def render_button(key, callback, root):
    def new_button():
        helv20 = font.Font(root=root.master, family="Helvetica", size=20, weight="bold")

        return tk.Button(root, bg="white", text=key, font=helv20, command=callback, width=1)

    if key == "0":
        new_button().place(relx=0.0, rely=0.895, relwidth=0.47, relheight=0.1)
    elif key == ".":
        new_button().place(relx=0.480, rely=0.895, relwidth=0.23, relheight=0.1)
    elif key == "1":
        new_button().place(relx=0.0, rely=0.790, relwidth=0.23, relheight=0.1)
    elif key == "2":
        new_button().place(relx=0.240, rely=0.790, relwidth=0.23, relheight=0.1)
    elif key == "3":
        new_button().place(relx=0.480, rely=0.790, relwidth=0.23, relheight=0.1)
    elif key == "4":
        new_button().place(relx=0.0, rely=0.685, relwidth=0.23, relheight=0.1)
    elif key == "5":
        new_button().place(relx=0.240, rely=0.685, relwidth=0.23, relheight=0.1)
    elif key == "6":
        new_button().place(relx=0.480, rely=0.685, relwidth=0.23, relheight=0.1)
    elif key == "7":
        new_button().place(relx=0.0, rely=0.580, relwidth=0.23, relheight=0.1)
    elif key == "8":
        new_button().place(relx=0.240, rely=0.580, relwidth=0.23, relheight=0.1)
    elif key == "9":
        new_button().place(relx=0.480, rely=0.580, relwidth=0.23, relheight=0.1)
    elif key == "=":
        new_button().place(relx=0.715, rely=0.840, relwidth=0.275, relheight=0.153)
    elif key == "+":
        new_button().place(relx=0.715, rely=0.685, relwidth=0.275, relheight=0.153)
    elif key == "*":
        new_button().place(relx=0.715, rely=0.530, relwidth=0.275, relheight=0.153)
    elif key == "÷":
        new_button().place(relx=0.715, rely=0.375, relwidth=0.275, relheight=0.153)
    elif key == "-":
        new_button().place(relx=0.715, rely=0.220, relwidth=0.275, relheight=0.153)
    elif key == "√x":
        new_button().place(relx=0.0, rely=0.475, relwidth=0.23, relheight=0.1)
    elif key == "xⁿ":
        new_button().place(relx=0.240, rely=0.475, relwidth=0.23, relheight=0.1)
    elif key == "n!":
        new_button().place(relx=0.480, rely=0.475, relwidth=0.23, relheight=0.1)
    elif key == "(":
        new_button().place(relx=0.0, rely=0.370, relwidth=0.23, relheight=0.1)
    elif key == "ABS":
        new_button().place(relx=0.240, rely=0.370, relwidth=0.23, relheight=0.1)
    elif key == ")":
        new_button().place(relx=0.480, rely=0.370, relwidth=0.23, relheight=0.1)
    elif key == "Clean":
        new_button().place(relx=0.00, rely=0.220, relwidth=0.47, relheight=0.145)
    elif key == "⌫":
        new_button().place(relx=0.480, rely=0.220, relwidth=0.23, relheight=0.145)
