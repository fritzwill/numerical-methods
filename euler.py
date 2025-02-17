# Will Fritz
# 12/4/2017
# Using Euler's Method to approcximate y(1) if the following IVP:
# (dy/dt) = 0.3 - 0.1y(t), 0 <= t <= 1
# y(0) = 0
import numpy as np
import math

# globals 
x0 = 0
y0 = 0
xf = 1
h = 0.2 # h = (xf-x0)/(n-1)
n = 6

# eqn used to describe (dy/dt) = f(x,y)
def f(x,y):
    return (0.3-0.1*y)

# initialize x and y
x = np.linspace(x0, xf, n)
y = np.zeros([n])

# initial values
y[0] = y0
w = y0

# populate y using Eulers Method
for i in range(1, n):
    y[i] = h*(f(0,w)) + w
    w = y[i]
    print("w({}) = {}".format(i, y[i]))

yApprox = y[-1]
yExact = -3*math.exp(-0.1*(1))+3

print("\nApproximation for y(1) with h = 0.2:   y(1) = {}".format(yApprox))
print("Exact y(1):   y(1) = {}".format(yExact))

print("\nRelative accuracy: abs((yApprox - yExact)/yExact)")
print("Relative accuracy = {}".format(abs((yApprox - yExact)/yExact)))
