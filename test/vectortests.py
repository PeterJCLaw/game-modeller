
import unittest

import util
from point import Point, Vector
from arena import Arena

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

#        self.assertIsInstance(p2, Point)
        util.assertEqual(Point(2, 1), p2)


if __name__ == '__main__':
    unittest.main(buffer=True)
