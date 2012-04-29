
from cmath import phase, pi, polar, rect

from point import Vector

def angle_between(a, b):
    a_phase = phase(a)
    b_phase = phase(b)
    angle = abs(a_phase - b_phase)
    while angle > pi:
        angle -= pi
    return angle

def midpoint(a, b):
    return (a + b) / 2

def length_towards(length, target):
    """
    Return a Vector that has length 'length',
    in the same direction as 'target'.
    """

    (r, phi) = polar(target)
    c = rect(length, phi)
    v = Vector(c.real, c.imag)
    return v
