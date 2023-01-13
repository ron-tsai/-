import numpy as np
import matplotlib.pyplot as plt

size = 5
x = np.arange(size)
# a = np.random.random(size)
# b = np.random.random(size)
a=[53.15,59.68,51.51,55.10,56]
c=[56.98,59.72,71.87,65.18,56]
b=[]
for i in range(len(a)):
    c1 = c[i] - a[i]

    b.append(c1)

plt.bar(x, a, label='a')
plt.bar(x, b, bottom=a, label='b')
plt.legend()
plt.show()