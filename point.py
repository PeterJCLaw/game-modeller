
class Point(object):
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

	def __eq__(self, other):
		return isinstance(other, type(self)) and self.x == other.x and self.y == other.y

	def __ne__(self, other):
		return not isinstance(other, type(self)) or self.x != other.x or self.y != other.y

	def __hash__(self):
		return hash(self.x) ** hash(self.y)

	def __repr__(self):
		return "Point(%d, %d)" % (self.x, self.y)
