
from point import Point

class Arena(object):
	def __init__(self, width, height):
		self._width = width
		self._height = height

	@property
	def width(self):
		return self._width

	@property
	def height(self):
		return self._height

	def corner_location(self, id):
		x = self._width * int(id / 2)
		y = self._height * ( id == 1 or id == 2 )
		return Point(x, y)
