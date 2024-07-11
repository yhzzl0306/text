import matplotlib.pyplot as plt
from numpy import *

x = arange(-2 * pi, 2 * pi, 0.01)
y = sin(x)

plt.figure()
plt.plot(x, y)
plt.grid(True)
plt.show()