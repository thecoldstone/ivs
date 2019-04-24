#!/usr/bin/env python
# -*- coding: utf-8 -*

from src.staff.math_api import add, sub, multiply, absolute, divide, factorial, absolute, power

import math
import unittest


class Tests(unittest.TestCase):

    def testAdd(self):
        self.assertEqual(12 + 6, add(12, 6))
        self.assertEqual(10.25 + (-5.36), add(10.25, -5.36))
        self.assertEqual(0 + 5698, add(0, 5698))

    def testSub(self):
        self.assertEqual(12 - 6, sub(12, 6))
        self.assertEqual(10.25 - (-5.36), sub(10.25, -5.36))
        self.assertEqual(0 - 5698, sub(0, 5698))

    def testMul(self):
        self.assertEqual(12 * 6, multiply(12, 6))
        self.assertEqual(10.25 * (-5.36), multiply(10.25, -5.36))
        self.assertEqual(0 * 5698, multiply(0, 5698))

    def testDiv(self):
        self.assertEqual(12 / 6, divide(12, 6))
        self.assertEqual(10.25 / (-5.36), divide(10.25, -5.36))
        self.assertEqual(0 / 5698, divide(0, 5698))
        self.assertEqual('nan', divide(0, 0))

    def testFact(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(math.factorial(888), factorial(888))

    def testAbs(self):
        self.assertEqual(abs(-0), absolute(0))
        self.assertEqual(abs(6.3258), absolute(6.3258))
        self.assertEqual(abs(6.3258), absolute(-6.3258))

    def testPower(self):
        self.assertEqual((math.pow(2, 6)), power(2, 6))
        self.assertEqual((math.pow(2, 6.25)), power(2, 6.25))
        self.assertEqual((math.pow(-2, -32)), power(-2, -32))
        self.assertEqual(1, power(258, 0))


if __name__ == '__main__':
    unittest.main()
