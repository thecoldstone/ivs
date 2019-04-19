import random

def PickColors():
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "black", "white", "purple", "grey"]
    col1 = random.choice(colors)
    col2 = random.choice(colors)
    if col1 == col2:
        return PickColors()
    return col1, col2
    #return PickColors() if col1 == col2 else col1, col2

def PickColor():
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "black", "white", "purple", "grey"]
    col12 = random.choice(colors)
    return  col12

