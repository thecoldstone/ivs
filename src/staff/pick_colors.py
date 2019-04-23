import random


def pick_colors():
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "black", "white", "purple", "grey"]
    col1 = random.choice(colors)
    col2 = random.choice(colors)
    if col1 == col2:
        return pick_colors()
    return col1, col2
