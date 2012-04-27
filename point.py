
class Point(complex):
	def __init__(self, x = 0, y = 0):
		super(Point, self).__init__(x, y)

	def __repr__(self):
		return "Point(%d, %d)" % (self.x, self.y)

	@property
	def x(self):
		return self.real

	@property
	def y(self):
		return self.imag

class Vector(Point):
	def __repr__(self):
		return "Vector(%d, %d)" % (self.x, self.y)
