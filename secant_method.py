def dx(x):
    return 4 * x**3 - 1
def fx(x):
    return x**4 - x - 10

xn = 1
xnn = 1.5
count = 0

while(abs(fx(xnn)) > 0.00001):
    print(count, ":", xnn, xn)
    tmp = xnn
    xnn = xn - (xnn - xn)/(fx(xnn)- fx(xn)) *fx(xn)
    xn = tmp
    count += 1
