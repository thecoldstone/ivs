import tkinter as tk  # py3

from src.staff.GradientFrame import GradientFrame


class Window(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        GradientFrame(self, borderwidth=1, relief="sunken").pack(side="top", fill="both", expand=True)
