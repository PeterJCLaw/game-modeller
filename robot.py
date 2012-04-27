
from point import Point

from datetime import timedelta, datetime
import time

class Robot(object):
	_speed = 0.1

	def __init__(self, id, match, arena):
		self._id = id
		self._match = match
		self._arena = arena
		self._opponents = set()
		self._location = Point()

	@property
	def location(self):
		return self._location

	def addOpponents(self, robots):
		for r in robots:
			if not r is self:
				self._opponents.add(r)

	def run(self, corner, args = None):
		self._location = self._arena.corner_location(corner)
		self._match.waitForStart()
#		print 'Game started: %d' % self._id

		while True:
			target = self.getTarget()
			self.moveTowards(target)

	def moveTowards(self, target):
		"""
		Move towards the given Point for about a second
		"""

		dist = target * self._speed

		end = datetime.now() + timedelta(seconds = 1)
		while datetime.now() < end:
			time.sleep(0.1)
			self._location = self.location + dist

	def getTarget(self):
		"Figure out where to move towards"
		# move towards the middle of the arena
		return Point(self._arena.width / 2, self._arena.height / 2)
