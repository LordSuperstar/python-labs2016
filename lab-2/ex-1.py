import numpy as np
x=1
a=np.exp(1/(np.sin(x) + 1))
b=5/4 + 1/(x**15)
c=np.math.log(a/b, 1+x**2)
print('y = ', a, 'x = 1')

x=10
a=np.exp(1/(np.sin(x) + 1))
b=5/4 + 1/(x**15)
c=np.math.log(a/b, 1+x**2)
print('y = ', a, 'x = 10')

x=100
a=np.exp(1/(np.sin(x) + 1))
b=5/4 + 1/(x**15)
c=np.math.log(a/b, 1+x**2)
print('y = ', a, 'x = 100')

# Why the programm doesn't work with np.log?
# It works only with np.math.log