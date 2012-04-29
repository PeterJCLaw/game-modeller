
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


    def test_limits_origin(self):
        p = Point(0,0)
        valid = self._arena.position_valid(p)
        util.assertTrue(valid)

    def test_limits_max(self):
        p = Point(8, 8)
        valid = self._arena.position_valid(p)
        util.assertTrue(valid)

    def test_limits_neg(self):
        p = Point(8, -8)
        valid = self._arena.position_valid(p)
        util.assertFalse(valid)

    def test_limits_pos(self):
        p = Point(8, 16)
        valid = self._arena.position_valid(p)
        util.assertFalse(valid)

    def test_limits_neg2(self):
        p = Point(-8, 0)
        valid = self._arena.position_valid(p)
        util.assertFalse(valid)

    def test_limits_pos2(self):
        p = Point(16, 0)
        valid = self._arena.position_valid(p)
        util.assertFalse(valid)

if __name__ == '__main__':
    unittest.main(buffer=True)
