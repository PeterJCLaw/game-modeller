
import unittest

import util
from mid_point_robot import MidPointRobot
from point import Point

class MidPointRobotTests(unittest.TestCase):

    def test_get_target_bots_unique(self):
        """Test that each bot gets a unique set of targets"""

        bots = []
        for i in xrange(4):
            bots.append(MidPointRobot(i, None, None))

        targets = []
        for bot in bots:
            bot.add_opponents(bots)
            targets.append(set(bot.get_target_bots()))

        for i in xrange(len(targets)):
            for j in xrange(len(targets)):
                if i == j:
                    continue
                util.assertNotEqual(targets[i], targets[j], "Comparing %d to %d", i, j)

if __name__ == '__main__':
    unittest.main(buffer=True)
