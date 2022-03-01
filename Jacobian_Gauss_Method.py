import numpy as np
def dist(a,b):
    a[0] = a[0] - b[0]
    a[1] = a[1] - b[1]
    a[2] = a[2] - b[2]
    return (a[0]**2 + a[1]**2 + a[2]**2)**0.5 
def jacobi(v):
  tmp = np.array([-1.0,2.0,3.0])
  r = np.array([0,-2.0,3.0,-3.0,0,1.0,2.0,-2.0,0])
  r = r.reshape((3,3)).copy()
  v = tmp - np.dot(r,v)

  out = np.array([0.0,0.0,0.0])
  out[0] = v[0]/5
  out[1] = v[1]/9
  out[2] = -v[2]/7
  
  return out

