#!/usr/bin/env python

import unittest

from point import Point
from arena import Arena
import util

class PointTests(unittest.TestCase):

	def _assertEqual(self, a, b):
		assert a == b
		assert (a != b) == False

	def _assertNotEqual(self, a, b):
		assert a != b
		assert (a == b) == False

	def testProperties(self):
		p = Point(0,9)
		self._assertEqual(p.x, 0)
		self._assertEqual(p.y, 9)

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

class ArenaTests(unittest.TestCase):

	def setUp(self):
		self._arena = Arena(8, 8)

	def testCorner0(self):
		p = self._arena.corner_location(0)
		util.assertEqual(Point(0,0), p)

	def testCorner1(self):
		p = self._arena.corner_location(1)
		util.assertEqual(Point(0,8), p)

	def testCorner2(self):
		p = self._arena.corner_location(2)
		util.assertEqual(Point(8,8), p)

	def testCorner3(self):
		p = self._arena.corner_location(3)
		util.assertEqual(Point(8,0), p)

if __name__ == '__main__':
	unittest.main(buffer=True)
