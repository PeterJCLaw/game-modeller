
import unittest

import util
from point import Point, Vector

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


if __name__ == '__main__':
    unittest.main(buffer=True)
