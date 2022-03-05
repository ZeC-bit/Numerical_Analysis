from numpy import poly1d as pd
import numpy as np
def newton(l):
#    print(l)
    if(len(l) == 1):
        return l[0][1]
    if(len(l) == 2): # [1,2] == f(1)- f(2) / 1 -2
        return (l[1][1] - l[0][1])/(l[1][0]-l[0][0])
    else:
        return (newton(l[1:])-newton(l[:-1]))/(l[-1][0] - l[0][0])
def poly(l):
    out = pd([l[0][1]])
    tmp = pd([1])
    for p in range(1,len(l)):
        for q in range(p):
            tmp = np.polymul(tmp, pd([1,-l[q][0]])) # producing pi of x-xj
        out = out + newton(l[:p+1]) * tmp 
        tmp = pd([1])
    return out

l = [(0,-6),(0.1,-5.89483),(0.3,-5.65014),(0.6,-5.17788),(1,-4.28172)]
print(poly(l))
for p in range(len(l)):
    for q in range(p):
        print(p,q,":",newton(l[p-q:p+1]),l[p-q:p+1])
