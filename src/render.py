import tkinter as tk  # py3

places = {
    "0": {
        "relx": 0.0, "rely": 0.895,
        "relwidth": 0.47,
        "relheight": 0.1
    }
}



def render_button(key, callback, root):
    def create_button():
        return tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1)
    if key == "0":
        tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1).place(relx=0.0, rely=0.895,
                                                                                             relwidth=0.47,
                                                                                             relheight=0.1)
    if key == ".":
        tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1).place(relx=0.480, rely=0.895,
                                                                                             relwidth=0.23,
                                                                                             relheight=0.1)
    if key == "1":
        tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1).place(relx=0.0, rely=0.790,
                                                                                             relwidth=0.23,
                                                                                             relheight=0.1)
    if key == "2":
        tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1).place(relx=0.240, rely=0.790,
                                                                                             relwidth=0.23,
                                                                                             relheight=0.1)
    if key == "3":
        tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1).place(relx=0.480, rely=0.790,
                                                                                             relwidth=0.23,
                                                                                             relheight=0.1)
    if key == "4":
        tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1).place(relx=0.0, rely=0.685,
                                                                                             relwidth=0.23,
                                                                                             relheight=0.1)
    if key == "5":
        tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1).place(relx=0.240, rely=0.685,
                                                                                             relwidth=0.23,
                                                                                             relheight=0.1)
    if key == "6":
        tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1).place(relx=0.480, rely=0.685,
                                                                                             relwidth=0.23,
                                                                                             relheight=0.1)
    if key == "7":
        tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1).place(relx=0.0, rely=0.580,
                                                                                             relwidth=0.23,
                                                                                             relheight=0.1)
    if key == "8":
        tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1).place(relx=0.240, rely=0.580,
                                                                                             relwidth=0.23,
                                                                                             relheight=0.1)
    if key == "9":
        tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1).place(relx=0.480, rely=0.580,
                                                                                             relwidth=0.23,
                                                                                             relheight=0.1)
    if key == "=":
        tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1).place(relx=0.715, rely=0.840,
                                                                                             relwidth=0.275,
                                                                                             relheight=0.153)
    if key == "+":
        tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1).place(relx=0.715, rely=0.685,
                                                                                             relwidth=0.275,
                                                                                             relheight=0.153)
    if key == "*":
        tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1).place(relx=0.715, rely=0.530,
                                                                                             relwidth=0.275,
                                                                                             relheight=0.153)
    if key == "÷":
        tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1).place(relx=0.715, rely=0.375,
                                                                                             relwidth=0.275,
                                                                                             relheight=0.153)
    if key == "-":
        tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1).place(relx=0.715, rely=0.220,
                                                                                             relwidth=0.275,
                                                                                             relheight=0.153)
    if key == "√x":
        tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1).place(relx=0.0, rely=0.475,
                                                                                             relwidth=0.23,
                                                                                             relheight=0.1)
    if key == "xⁿ":
        tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1).place(relx=0.240, rely=0.475,
                                                                                             relwidth=0.23,
                                                                                             relheight=0.1)
    if key == "n!":
        tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1).place(relx=0.480, rely=0.475,
                                                                                             relwidth=0.23,
                                                                                             relheight=0.1)
    if key == "(":
        tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1).place(relx=0.0, rely=0.370,
                                                                                             relwidth=0.23,
                                                                                             relheight=0.1)
    if key == "ABS":
        tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1).place(relx=0.240, rely=0.370,
                                                                                             relwidth=0.23,
                                                                                             relheight=0.1)
    if key == ")":
        tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1).place(relx=0.480, rely=0.370,
                                                                                             relwidth=0.23,
                                                                                             relheight=0.1)
    if key == "Clean":
        tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1).place(relx=0.00, rely=0.220,
                                                                                             relwidth=0.47,
                                                                                             relheight=0.145)
    if key == "⌫":
        tk.Button(root, bg="white", text=key, font="Arial", command=callback, width=1).place(relx=0.480, rely=0.220,
                                                                                             relwidth=0.23,
                                                                                             relheight=0.145)
