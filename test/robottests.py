
import unittest
from datetime import datetime, timedelta

import util
from robot import Robot
from point import Point

class RobotMoveTests(unittest.TestCase):

    def setUp(self):
        self._robot = Robot(0, None, None)
        self._target = Point(0,4)

    def testEndLocation(self):
        # TODO: expose these?
        r = self._robot
        r._speed = 0.1
        r._updateDelay = 0.1
        r._moveDuration = 1

        r.move_towards(self._target)
        l = r.location

        # Round to something sensible
        l = Point(round(l.x, 5), round(l.y, 5))

        # Moved at 0.1 m/s for 1s
        util.assertEqual(Point(0, 0.1), l)

    def testEndLocation2(self):
        # TODO: expose these?
        r = self._robot
        r._speed = 0.1
        r._updateDelay = 0.1
        r._moveDuration = 1

        r.move_towards(Point(10, 0))
        l = r.location

        # Round to something sensible
        l = Point(round(l.x, 5), round(l.y, 5))

        # Moved at 0.1 m/s for 1s
        util.assertEqual(Point(0.1, 0), l)

    def testDuration(self):
        start = datetime.now()
        self._robot.move_towards(self._target)
        end = datetime.now()

        dur = end - start

        self.assertAlmostEqual(1.0, dur.seconds)

if __name__ == '__main__':
    unittest.main(buffer=True)
