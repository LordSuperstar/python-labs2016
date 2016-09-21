import matplotlib.pyplot as plt
import numpy as np
import math

x=np.arange(-2, 2, 0.001)
z=1
# i=1
# while i < math.inf:
for i in range(500):
    y=(0.25**i)*np.cos((3**i)*np.pi*x)
    z+=y
plt.plot(x, z)
plt.show()

# while True: