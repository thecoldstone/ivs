import tkinter as tk  # py3
from tkinter import font


def validate(self, action, index, value_if_allowed,
             prior_value, text, validation_type, trigger_type):
    try:
        float(prior_value)
        return True
    except ValueError:
        return False


def create_entry(root):
    helv20 = font.Font(root=root.master, family="Helvetica", size=20)
    vcmd = (root.register(validate),
            '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
    entry_input = tk.Entry(root, font=helv20, bg="white", validate='key', validatecommand=vcmd)
    entry_input.place(relx=0.01, rely=0.01, relheight=0.1, relwidth=0.98)

    return entry_input
