
import json
import sys
import time
from threading import Thread, Event

from arena import Arena
from robot import Robot
from dict_converters import *

class Match(object):

	def __init__(self):
		# Game start lock
		self._game_start = Event()

		self._robots = []
		arena = Arena(8.0, 8.0)

		for i in range(4):
			r = Robot(i, self, arena)
			self._robots.append(r)
			t = Thread( target = r.run, args = (i, ) )
			t.start()

		for r in self._robots:
			r.addOpponents(self._robots)

	def waitForStart(self):
		assert self._game_start.wait(3)

	def start(self):
		"Start the game"
		self._game_start.set()

		while True:
			for r in self._robots:
				rd = robot_to_dict(r)
				print json.dumps(rd)
				sys.stdout.flush()
			time.sleep(0.1)

if __name__ == '__main__':
	m = Match()
	m.start()
