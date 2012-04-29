
import unittest
from math import pi

import util
from point import Point
from vector_maths import angle_between

class VectorMathsTests(unittest.TestCase):

    def setUp(self):
        self._a = Point(0, 4)
        self._b = Point(4, 0)
        self._c = Point(0, -4)
        self._d = Point(-4, 0)

    def test_angle_self(self):
        angle = angle_between(self._a, self._a)
        self.assertEqual(0, angle)

    def test_angle_forwards(self):
        angle = angle_between(self._a, self._b)
        self.assertAlmostEqual(pi/2, angle)

    def test_angle_backwards(self):
        angle = angle_between(self._b, self._a)
        self.assertAlmostEqual(pi/2, angle)

    def test_angle_forwards2(self):
        angle = angle_between(self._c, self._d)
        self.assertAlmostEqual(pi/2, angle)

    def test_angle_backwards2(self):
        angle = angle_between(self._c, self._d)
        self.assertAlmostEqual(pi/2, angle)

    def test_wide_angle_forwards(self):
        angle = angle_between(self._a, self._c)
        self.assertAlmostEqual(pi, angle)

    def test_wide_angle_backwards(self):
        angle = angle_between(self._c, self._a)
        self.assertAlmostEqual(pi, angle)

    def test_wide_angle_forwards2(self):
        angle = angle_between(self._b, self._d)
        self.assertAlmostEqual(pi, angle)

    def test_wide_angle_backwards2(self):
        angle = angle_between(self._d, self._b)
        self.assertAlmostEqual(pi, angle)


if __name__ == '__main__':
    unittest.main(buffer=True)
