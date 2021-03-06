
import json
import sys
import time
from threading import Thread, Event

from arena import Arena
from debug_writer import DebugWriter
from dict_converters import *
from robot import Robot
from mid_point_robot import MidPointRobot

class Match(object):
    def __init__(self, robot_count = 4, robot_type = Robot, robots = None, arena = None):
        # Game start lock
        self._game_start = Event()

        if arena is None:
            arena = Arena(8.0, 8.0)

        self._robots = []
        if robots is not None:
            self._robots = robots

        robots_needed = max( 0, robot_count - len(self._robots) )
        for i in xrange(robots_needed):
            r = robot_type(i, self, arena)
            self._robots.append(r)

        for i in xrange(robot_count):
            r = self._robots[i]
            t = Thread( target = r.run, args = (i, ) )
            t.start()

            r.add_opponents(self._robots)

        self._out = sys.stdout
        sys.stdout = DebugWriter(sys.stdout)

    def _json_print(self, data):
        print >> self._out, json.dumps(data)
        self._out.flush()

    def _print_state(self):
        for r in self._robots:
            rd = robot_to_dict(r)
            self._json_print(rd)

    def end(self):
        self._json_print(dict(type = 'match', state = 'end'))
        for r in self._robots:
            r.stop()

    def wait_for_start(self):
        assert self._game_start.wait(3)

    def start(self, duration = 180):
        """Start the game."""
        md = dict(type = 'match', state = 'start', robots = len(self._robots))
        self._json_print(md)
        self._print_state()
        self._game_start.set()

        for i in xrange(10 * duration):
            self._print_state()
            time.sleep(0.1)

if __name__ == '__main__':
    m = Match(4, robot_type = MidPointRobot)
    try:
        m.start()
    finally:
        m.end()
