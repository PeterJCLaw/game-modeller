
import unittest
from math import pi

import util
from point import Point, Vector
from vector_maths import angle_between, midpoint, length_towards

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


    def test_midpoint(self):
        exp = Point(0, 0)
        mid = midpoint(self._a, self._c)
        util.assertEqual(exp, mid)

    def test_midpoint2(self):
        exp = Point(2, 2)
        mid = midpoint(self._a, self._b)
        util.assertEqual(exp, mid)


    def test_length_towards(self):
        exp = Vector(0, 2)
        actual = length_towards(2, self._a)
        actual = Vector(round(actual.x, 5), round(actual.y, 5))
        util.assertEqual(exp, actual)

    def test_length_beyond(self):
        exp = Vector(0, 8)
        actual = length_towards(8, self._a)
        actual = Vector(round(actual.x, 5), round(actual.y, 5))
        util.assertEqual(exp, actual)

if __name__ == '__main__':
    unittest.main(buffer=True)
