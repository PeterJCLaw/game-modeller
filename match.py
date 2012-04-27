
from threading import Thread, Event

from arena import Arena
from robot import Robot

class Match(object):

	def __init__(self):
		# Game start lock
		self._game_start = Event()

		robots = []
		arena = Arena(8.0, 8.0)

		for i in range(4):
			r = Robot(i, self, arena)
			robots.append(r)
			t = Thread( target = r.run, args = (i, ) )
			t.start()

		for r in robots:
			r.addOpponents(robots)

	def waitForStart(self):
		self._game_start.wait()

	def start(self):
		"Start the game"
		self._game_start.set()

if __name__ == '__main__':
	m = Match()
	m.start()

	sleep(180)	# 3 minute match

	exit()
