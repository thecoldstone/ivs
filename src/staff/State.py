from decimal import Decimal
import tkinter as tk

from src.staff import math_api


class State:
    _entry_input = None
    _left_operand = 0
    _operator = None
    _operator_just_used = False

    def __init__(self, entry_input):
        self._left_operand = 0
        self._operator = None
        self._entry_input = entry_input
        self.zero()

    def zero(self):
        self.refresh_right_slot_if_needed()
        if not self._entry_input.get() == "0":
            self._entry_input.insert(tk.END, "0")

    def dot(self):
        self.refresh_right_slot_if_needed()
        if "." not in self._entry_input.get():
            self._entry_input.insert(tk.END, ".")

    def digit(self, digit):
        if self._entry_input.get() == "0":
            self._entry_input.delete(0, tk.END)
        self.refresh_right_slot_if_needed()
        self._entry_input.insert(tk.END, digit)

    def backspace(self):
        if not self._entry_input.get() == "0":
            self._entry_input.delete(len(self._entry_input.get()) - 1, tk.END)

    def clean(self):
        self._left_operand = 0
        self._operator = None
        self._entry_input.delete(0, tk.END)
        self.zero()

    def op_plus(self):
        self.prepare_binary_operation(math_api.add)

    def op_minus(self):
        self.prepare_binary_operation(math_api.sub)

    def op_multiply(self):
        self.prepare_binary_operation(math_api.multiply)

    def op_divide(self):
        self.prepare_binary_operation(math_api.divide)

    def op_power(self):
        self.prepare_binary_operation(math_api.power)

    def op_root(self):
        self.prepare_binary_operation(math_api.root)

    def op_absolute(self):
        self.prepare_unary_operation(lambda _, number: math_api.absolute(number))

    def op_factorial(self):
        self.prepare_unary_operation(lambda _, number: math_api.factorial(number))

    def op_sign_switch(self):
        self.prepare_unary_operation(lambda _, number: -number)

    def op_equal(self):
        if self._operator is not None:
            self.calculate()
        self.copy_right_slot()
        self._operator_just_used = True

    def get_right_operand(self):
        return Decimal(self._entry_input.get())

    def calculate(self):
        result = self._operator(self._left_operand, self.get_right_operand())
        # clean everything
        self._operator = None
        self._entry_input.delete(0, tk.END)
        # save result in both slots
        self._left_operand = result
        self._entry_input.insert(tk.INSERT, str(result))

    def refresh_right_slot_if_needed(self):
        if self._operator_just_used:
            self._operator_just_used = False
            self._entry_input.delete(0, tk.END)

    def copy_right_slot(self):
        self._left_operand = self.get_right_operand()

    def prepare_binary_operation(self, operation):
        if not (self._left_operand == 0 or self._operator_just_used):
            self.calculate()
        self._operator = operation
        self.copy_right_slot()
        self._operator_just_used = True

    def prepare_unary_operation(self, operation):
        self._operator = operation
        self.calculate()
        self.copy_right_slot()
        self._operator_just_used = True
