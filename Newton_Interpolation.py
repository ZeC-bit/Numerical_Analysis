from numpy import poly1d

def f(x):
    return float(1/(1 + x * x))
def x(k,n):
    return -5 + float(10 / n) * k
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
    for i in range(0, 2 * n):
        print("When x =",x(i,2 * n)," Original:", f(x(i, 2 * n)),"  Interpolation :", np(x(i, 2 * n)))    
def error(n):
    p = poly1d([0])
    np = newton(0,n,p)
    print("Error when n =",n," at 1 + root(10):", abs(np(1+10**0.5) - f(1+ 10**0.5)))
    print()
    
def result(n):
    display(n)
    error(n)

result(2)
result(4)
result(8)
result(12)
result(30)
