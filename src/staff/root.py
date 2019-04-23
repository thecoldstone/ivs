import tkinter as tk  # py3

from src.staff.Window import Window


def create_root():
    root = tk.Tk()
    Window(root).pack(fill="both", expand=True)
    root.title("Calculator")
    root.geometry("600x600")

    return root
