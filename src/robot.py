
from point import Point

from datetime import timedelta, datetime
import time

class Robot(object):
    # Speed (m/s)
    _speed = 0.1

    # How often to update position (seconds)
    _updateDelay = 0.1

    # How long to move for, before re-evaluating the target (seconds)
    _moveDuration = 1

    def __init__(self, id, match, arena):
        self._id = id
        self._match = match
        self._arena = arena
        self._opponents = set()
        self._location = Point()
        self._end = False

    @property
    def id(self):
        return self._id

    @property
    def location(self):
        return self._location

    def add_opponents(self, robots):
        for r in robots:
            if not r is self:
                self._opponents.add(r)

    def stop(self):
        self._end = True

    def run(self, corner, args = None):
        self._location = self._arena.corner_location(corner)
        self._match.wait_for_start()
#        print 'Game started: %d' % self._id

        while not self._end:
            target = self.get_target()
            self.move_towards(target)

    def move_towards(self, target):
        """
        Move towards the given Point for about a second
        """

        to_move = (target-self._location)
#        print 'to_move', to_move
        dist = to_move * self._speed
#        print 'dist', dist

        end = datetime.now() + timedelta(seconds = self._moveDuration)
        while datetime.now() < end:
#            print 'Location', self._location
            time.sleep(self._updateDelay)
            self._location = self._location + dist * self._updateDelay

    def get_target(self):
        """
        Figure out where to move towards.
        This is the interesting part of the robot's implementation
        """
        # move towards the middle of the arena
        return Point(self._arena.width / 2, self._arena.height / 2)
