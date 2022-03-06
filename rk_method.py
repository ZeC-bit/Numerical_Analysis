#function is given to be y' = t* sqrt(y)
#t value changes from 0 to 10 over iteration
from math import sqrt
import matplotlib.pyplot as plt

def f(t, y):
    return t * sqrt(y)
def rk4(f, t0, y0, t1, n):
    vt = (n + 1) * [0]
    vy = (n + 1) * [0]
    h = float((t1 - t0) /n)
    vt[0] = t0
    vy[0] = y0
    t = t0
    y = y0
    for i in range(1, n + 1):
        k1 = h * f(t, y)
        k2 = h * f(t + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(t + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(t + h, y + k3)
        t = t0 + i * h
        vt[i] = t
        y = y + (k1 + k2 + k2 + k3 + k3 + k4) / 6
        vy[i] = y
    return vt, vy
