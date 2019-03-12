from tkinter import *
from main import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Kalkulacka")

        self.total = 0
        self.entered_number = 0

        self.label_text = IntVar()

        self.label = Label(master, text="Total: ")

        # LAYOUT

        self.label.grid(row = 0, column = 0, sticky = W)

        (Ass()).ass()



root = Tk()
my_gui = Calculator(root)
root.mainloop()