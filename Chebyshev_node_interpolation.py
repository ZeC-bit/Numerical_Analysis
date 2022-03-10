from numpy import poly1d
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return float(1/(1 + x * x))
def x(k,n):
    return 5 * np.cos((2 * k + 1) / (2 * n + 2) * np.pi)
def newton(k,n,p): 
    ptmp = poly1d([1])
    for i in range(0,k):
        ptmp = ptmp * poly1d([1,-x(i, n)])
    c = (f(x(k,n)) - p(x(k,n))) / ptmp(x(k,n))
    p = p + ptmp * c
    if (k == n):
        return p
    else:
        return newton(k+1, n, p)
def display(n):
    p = poly1d([0])
    np = newton(0,n,p)
    xvalue = []
    fx = []
    for i in range(0, 2 * n):
        xvalue = xvalue + [x(i,2 * n)]
        fx = fx + [np(x(i, 2 * n))]
    plt.plot(xvalue, fx)
    plt.ylabel('polynomial approximate value')
def error(n):
    p = poly1d([0])
    np = newton(0,n,p)
    return [abs(np(1+10**0.5) - f(1+ 10**0.5))]
    
def result(n):
    display(n)
    return error(n)

err = result(2)
err = err + result(4)
err = err + result(8)
err = err + result(16)
err = err + result(32)
plt.plot([2,4,8,16,32], err)

