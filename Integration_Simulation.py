import numpy as np
import math
def apply(l, f):
  return [f(float(element)) for element in l]
nlist = [10,100,1000,10000]
for n in nlist:
  x =np.random.rand(n,1)
  x = apply(x, lambda k:(math.e**k -1)/k)
  print("When n = "+ str(n) + " approximation is " + str(np.mean(x)))
