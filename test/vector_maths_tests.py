
import unittest
from math import pi

import util
from point import Point
from vector_maths import angle_between

class VectorMathsTests(unittest.TestCase):

    def setUp(self):
        self._a = Point(0, 4)
        self._b = Point(4, 0)

    def test_angle_self(self):
        angle = angle_between(self._a, self._a)
        self.assertEqual(0, angle)

    def test_angle_forwards(self):
        angle = angle_between(self._a, self._b)
        self.assertAlmostEqual(pi/2, angle)

    def test_angle_backwards(self):
        angle = angle_between(self._b, self._a)
        self.assertAlmostEqual(pi/-2, angle)


if __name__ == '__main__':
    unittest.main(buffer=True)
