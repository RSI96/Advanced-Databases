import math
import numpy as np
from numpy.linalg import inv
from numpy.linalg import det
import matplotlib.pyplot as plt 



k = 1240/math.sqrt(7)
m = 4467
l = 2j
d = k+m
c = d+l

print("%.3f" % d)
print("%.20f" % d)

r = 17
h = 33
S = 2*math.pi*r**2 + 2*math.pi*r*h

"""
Multiline comment
"""
#line comment
'\ndasd\n'

x1 = 1
t = 1
r = 1

B = ((x1+r)/(r*math.sin(2*x1)+3.3456))*x1**(t*r)

a = math.sqrt(2)
M1= [[a, 1, -a], [0, 1, 1], [-a, a, 1]]
print("Matrix:\n {0}".format(M1))

M = np.array([[a, 1, -a], [0, 1, 1], [-a, a, 1]])
print("Matrix:\n {0}".format(M))

Minv = inv(M)
Mtra = M.T
Mdet = det(M)
print("Matrix inverted:\n {0}".format(Minv))
print("Matrix transposited:\n {0}".format(Mtra))
print("Matrix determined:\n {0}".format(Mdet))

print("Element 1x1: {0}".format(M[0,0]))
print("Element 3x3: {0}".format(M[2,2]))
print("Element 3x2: {0}".format(M[2,1]))

print("Vector 1:\n {0}".format(M[:,2]))
print("Vector 2:\n {0}".format(M[1,:]))

coeff = [1, -7, 3, 43, -28, -60]
roots = np.roots(coeff)

string1 = np.arange(1, 5, 1.5)
string2 = np.linspace(2.0, 3.0, num=5)
#string1 we define step, in string2 we define number of steps between values

def fun1(x):
    return x**2-3*x

x = np.linspace(-1,1)
y = fun1(x)
plt.plot(x, y)
plt.title('Chart (-1, 1)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend('Chart 1')
plt.show()

x = np.linspace(-5,5)
y = fun1(x)
plt.plot(x, y)
plt.title('Chart (-5, 5)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend('Chart 1')
plt.show()

x = np.linspace(-0,5)
y = fun1(x)
plt.plot(x, y)
plt.title('Chart (-0, 5)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend('Chart 1')
plt.show()

def Q(m, v):
    return (m*v**2)/2

m=2500
v=60
