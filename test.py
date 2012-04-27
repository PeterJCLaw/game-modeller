#!/usr/bin/env python

from point import Point
import unittest

class PointTests(unittest.TestCase):

	def _assertEqual(self, a, b):
		assert a == b
		assert (a != b) == False

	def _assertNotEqual(self, a, b):
		assert a != b
		assert (a == b) == False

	def testEquals(self):
		a = Point(0,9)
		b = Point(0,9)
		self._assertEqual(a, b)

	def testNotEqualsOther(self):
		a = Point(0,9)
		self._assertNotEqual(a, self)

	def testNotEqualsNone(self):
		a = Point(0,9)
		self._assertNotEqual(a, None)

	def testNotEqualsX(self):
		a = Point(0,0)
		b = Point(9,0)
		self._assertNotEqual(a, b)

	def testNotEqualsY(self):
		a = Point(0,0)
		b = Point(0,9)
		self._assertNotEqual(a, b)

	def testNotEqualsBoth(self):
		a = Point(0,0)
		b = Point(9,9)
		self._assertNotEqual(a, b)

if __name__ == '__main__':
	unittest.main(buffer=True)
