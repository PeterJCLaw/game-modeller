
from cmath import phase, pi

def angle_between(a, b):
    a_phase = phase(a)
    b_phase = phase(b)
    angle = abs(a_phase - b_phase)
    while angle > pi:
        angle -= pi
    return angle

def midpoint(a, b):
    return (a + b) / 2
