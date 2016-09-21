import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3, 4, 5]
y = [0.99, 0.49, 0.35, 0.253, 0.18]
t = np.arange(1.00, 5.00, 0.01)

# subplot 1
plt.subplot(121)
f = np.polyfit(x, y, 1)
p_f = np.poly1d(f)
plt.plot(x, y, '.', t, p_f(t))
fp, f = np.polyfit(x, y, deg=1, cov=True)
plt.errorbar(x, y, xerr=fp[0], yerr=fp[1])
plt.title(r'$deg=1$')

# subplot 2
plt.subplot(122)
s = np.polyfit(x, y, 2)
p_s = np.poly1d(s)
plt.plot(x, y, '.', t, p_s(t))
fs, s = np.polyfit(x, y, deg=2, cov=True)
plt.errorbar(x, y, xerr=fp[0], yerr=fs[1])
plt.title(r'$deg=2$')

plt.axis('equal')
plt.show()
