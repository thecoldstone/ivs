import tkinter as tk  # py3
from tkinter import font


def create_entry(root):
    helv20 = font.Font(root=root.master, family="Helvetica", size=20)
    entry_input = tk.Entry(root, font=helv20, bg="white")
    entry_input.place(relx=0.01, rely=0.01, relheight=0.1, relwidth=0.98)

    return entry_input
