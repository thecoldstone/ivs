#!/usr/bin/env python
# -*- coding: utf-8 -*

from math_api import add, sub, multiply, absolute, factorial, divide

import math 
import unittest

class Tests(unittest.TestCase):

	def test1(self):
		self.assertEqual(12 + 6, add(12, 6))
		self.assertEqual(10.25 + (-5.36), add(10.25, -5.36))
		self.assertEqual(0 + 5698, add(0,5698))

	def test2(self):
		self.assertEqual(12 - 6, sub(12, 6))
		self.assertEqual(10.25 - (-5.36), sub(10.25, -5.36))
		self.assertEqual(0 - 5698, sub(0,5698))

	def test3(self):
		self.assertEqual(12 * 6, multiply(12, 6))
		self.assertEqual(10.25 * (-5.36), multiply(10.25, -5.36))
		self.assertEqual(0 * 5698, multiply(0,5698))

	def test4(self):
		self.assertEqual(12 / 6, divide(12, 6))
		self.assertEqual(10.25 / (-5.36), divide(10.25, -5.36))
		self.assertEqual(0 / 5698, divide(0,5698))
		self.assertEqual('nan', divide(0,0))	

if __name__ == '__main__':
    unittest.main()
