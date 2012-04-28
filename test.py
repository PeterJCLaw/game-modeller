#!/usr/bin/env python

import unittest

from point import Point, Vector
from arena import Arena
import util

class VectorTests(unittest.TestCase):

	def setUp(self):
		self._v = Vector(3, 4)
		self._dbl = Vector(6, 8)
		self._hlf = Vector(1.5, 2)

	def testMod(self):
		modv = abs(self._v)
		util.assertEqual(5, modv)

	def testRMultiply(self):
		v = self._v * 2
		util.assertEqual(self._dbl, v)

	def testMultiply(self):
		v = 2 * self._v
		util.assertEqual(self._dbl, v)

	def testRDiv(self):
		v = self._v / 2
		util.assertEqual(self._hlf, v)

	def testDiv(self):
		def go():
			2 / self._v
		self.assertRaises(TypeError, go)

	def testVMultiply(self):
		def go():
			self._hlf * self._v
		self.assertRaises(TypeError, go)

	def testVDiv(self):
		def go():
			self._hlf / self._v
		self.assertRaises(TypeError, go)

	def testSub(self):
		p = Point(5,5)
		p2 = p - self._v

#		self.assertIsInstance(p2, Point)
		util.assertEqual(Point(2, 1), p2)

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

	def testSub(self):
		p1 = Point(5,5)
		p2 = Point(3,4)

		v = p1 - p2

		self.assertIsInstance(v, Vector)
		util.assertEqual(Vector(2, 1), v)


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
