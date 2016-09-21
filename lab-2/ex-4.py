import numpy as np
import matplotlib.pyplot as plt
import pylab

pylab.ion()

for a in range(1, 50, 1):
    t = np.arange(0, 2*np.pi, 0.01)
    pylab.clf()
    pylab.plot(np.sin(t + a), np.cos(2 * t))
    pylab.draw()
    pylab.pause(0.01)

pylab.close()