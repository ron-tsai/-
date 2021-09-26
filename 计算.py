import numpy as np

a=[-0.999999,1,0.5]
b=np.mean(a)/np.std(a,ddof=1)
print(b)
c1=[-1,0,1]
c2=[-1,0,1,0,0]
d1=np.std(c1,ddof=1)
d2=np.std(c2,ddof=1)
print(d1,d2)