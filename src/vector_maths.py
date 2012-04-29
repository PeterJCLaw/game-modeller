
from cmath import phase

def angle_between(a, b):
    a_phase = phase(a)
    b_phase = phase(b)
    return a_phase - b_phase
