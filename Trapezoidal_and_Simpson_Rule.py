# function is e^x * cos(x)
from numpy import poly1d
import numpy as np
import math
import matplotlib.pyplot as plt

def f(x):
    return math.exp(x)* np.cos(x)
def simpson(k, n):
    if(k == n - 1):
        return np.pi / n / 6 * (f(x(k,n)) + 4 * f((x(k+1,n)+ x(k,n))/2) + f(x(k+1,n)))
    else:
        return simpson(k+1,n) + np.pi / n / 6 * (f(x(k,n)) + 4 * f((x(k+1,n)+ x(k,n))/2) + f(x(k+1,n)))
def trapezoid(k, n):
    if(k == n - 1):
        return (f(x(k+1,n)) + f(x(k,n)))* np.pi / n / 2
    else:
        return trapezoid(k+1,n) + (f(x(k+1,n)) + f(x(k,n)))* np.pi / n / 2
def x(k,n):
    return np.pi * k / n
def simpson_err(n,err):
    err = err + [simpson(0,n) + 12.0703463164]
def trapezoid_err(n,err):
    err = err + [trapezoid(0,n) + 12.0703463164]

a = [2,4,8,16,32,64,128]
err = []
for i in a:
    simpson_err(i,err)
plt.plot(a,err)
plt.ylabel("Error of simpson rule")
for i in a:
    trapezoid_err(i,err)
plt.plot(a,err)
plt.ylabel("Error of trapezoid rule")
