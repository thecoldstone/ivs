def map_key_press(key, state):
    if key == "0":
        state.zero()

    elif key == ".":
        state.dot()

    elif key.isdigit():
        state.digit(key)

    elif key == "⌫":
        state.backspace()

    elif key == "Clean":
        state.clean()

    elif key == "+":
        state.op_plus()

    elif key == "-":
        state.op_minus()

    elif key == "*":
        state.op_multiply()

    elif key == "÷":
        state.op_divide()

    elif key == "xⁿ":
        state.op_power()

    elif key == "√x":
        state.op_root()

    elif key == "ABS":
        state.op_absolute()

    elif key == "n!":
        state.op_factorial()

    elif key == "+/-":
        state.op_sign_switch()

    elif key == "=":
        state.op_equal()
