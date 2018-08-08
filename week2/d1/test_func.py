# Intor to Python Testing
# Testing Taxonomies: https://wiki.python.org/moin/PythonTestingToolsTaxonomy

# Python unittest ref https://docs.python.org/3/library/unittest.html

import unittest

from func import woof

# woof(2)

class TestWoof(unittest.TestCase):

	def test0(self):
		self.assertEqual(woof(0), '')
	def test1(self):
		self.assertEqual(woof(1), 'woof ')
	def test2(self):
		self.assertEqual(woof(2), 'woof woof ')
	def test3(self):
		self.assertEqual(woof(3), 'woof woof woof ')

unittest.main()