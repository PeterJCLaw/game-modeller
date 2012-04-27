
from point import Point

class Robot(object):
	def __init__(self, id, game_start):
		self._id = id
		self._start = game_start
		self._opponents = set()

	def addOpponents(self, robots):
		for r in robots:
			if not r is self:
				self._opponents.add(r)

	def run(self, corner, args = None):
		self._start.wait()
		self._location = Point()
		print 'Game started: %d' % self._id
