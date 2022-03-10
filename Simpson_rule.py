import numpy as np
hlist = [16,64,256,1024]
h = np.pi
k = np.pi /2
out = 0 
for hh in hlist:
  h= h/ hh
  for i in range(int(k/h)):
    if(i % 2 == 0):
      out = out + 2 * np.sin(i*h)
    else:
      out = out + 4 * np.sin(i*h)
  out -= 1
  out = out * h /3
  print("When h = " + str(h) + " result = " + str(out))
  out = 0
  h = np.pi
