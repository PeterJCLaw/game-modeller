
class Vector(complex):
	def __init__(self, x = 0, y = 0):
		x = float(x)
		y = float(y)
		super(Vector, self).__init__(x, y)

	def __repr__(self):
		return "Vector(%.2f, %.2f)" % (self.x, self.y)

	def __str__(self):
		return self.__repr__()

	def __add__(self, other):
		if not isinstance(other, complex):
			return NotImplemented

		res = super(Vector, self).__add__(other)
		return Vector(res.real, res.imag)

	def __sub__(self, other):
		if not isinstance(other, complex):
			return NotImplemented

		res = super(Vector, self).__sub__(other)
		return Vector(res.real, res.imag)

	def __mul__(self, other):
		if isinstance(other, complex):
			return NotImplemented

		res = super(Vector, self).__mul__(other)
		return Vector(res.real, res.imag)

	def __floordiv__(self, other):
		if isinstance(other, complex):
			return NotImplemented

		res = super(Vector, self).__floordiv__(other)
		return Vector(res.real, res.imag)

	def __mod__(self, other):
		return NotImplemented

	def __divmod__(self, other):
		return NotImplemented

	def __div__(self, other):
		if isinstance(other, complex):
			return NotImplemented

		res = super(Vector, self).__div__(other)
		return Vector(res.real, res.imag)

	def __truediv__(self, other):
		if isinstance(other, complex):
			return NotImplemented

		res = super(Vector, self).__truediv__(other)
		return Vector(res.real, res.imag)

	def __pow__(self, other):
		return NotImplemented

	def __radd__(self, other):
		if not isinstance(other, complex):
			return NotImplemented

		res = super(Vector, self).__radd__(other)
		return Vector(res.real, res.imag)

	def __rsub__(self, other):
		if not isinstance(other, complex):
			return NotImplemented

		res = super(Vector, self).__rsub__(other)
		return Vector(res.real, res.imag)

	def __rmul__(self, other):
		if isinstance(other, complex):
			return NotImplemented

		res = super(Vector, self).__rmul__(other)
		return Vector(res.real, res.imag)

	def __rdiv__(self, other):
		return NotImplemented

	def __rtruediv__(self, other):
		return NotImplemented

	def __rfloordiv__(self, other):
		return NotImplemented

	def __rmod__(self, other):
		return NotImplemented

	def __rdivmod__(self, other):
		return NotImplemented

	def __rpow__(self, other):
		return NotImplemented

	@property
	def x(self):
		return self.real

	@property
	def y(self):
		return self.imag

class Point(Vector):
	def __repr__(self):
		return "Point(%.2f, %.2f)" % (self.x, self.y)

	def __mul__(self, other):
		return NotImplemented

	def __floordiv__(self, other):
		return NotImplemented

	def __div__(self, other):
		return NotImplemented

	def __truediv__(self, other):
		return NotImplemented

	def __rmul__(self, other):
		return NotImplemented
