import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-10, 10.01, 0.01)
a=1+np.tan(1/(1 + (np.sin(x)**2)))
b=(x**2 + 1)*(np.exp((np.abs(x))/(-1*10)))
plt.plot(x, np.log(b, a))
plt.show()