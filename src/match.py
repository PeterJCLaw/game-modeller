
import json
import sys
import time
from threading import Thread, Event

from arena import Arena
from robot import Robot
from dict_converters import *

class Match(object):

	def __init__(self, robots, arena = None):
		# Game start lock
		self._game_start = Event()

		self._robots = []
		if arena is None:
			arena = Arena(8.0, 8.0)

		for i in range(robots):
			r = Robot(i, self, arena)
			self._robots.append(r)
			t = Thread( target = r.run, args = (i, ) )
			t.start()

		for r in self._robots:
			r.addOpponents(self._robots)

	def _print_state(self):
		for r in self._robots:
			rd = robot_to_dict(r)
			print json.dumps(rd)
			sys.stdout.flush()

	def waitForStart(self):
		assert self._game_start.wait(3)

	def start(self, duration = 180):
		"Start the game"
		md = dict(type = 'match', robots = len(self._robots))
		print json.dumps(md)
		self._print_state()
		self._game_start.set()

		for i in xrange(10 * duration):
			self._print_state()
			time.sleep(0.1)

if __name__ == '__main__':
	# Small values for now
	m = Match(1)
	m.start(5)
