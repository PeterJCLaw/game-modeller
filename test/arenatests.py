
import unittest

import util
from arena import Arena
from point import Point

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
