#!/usr/bin/env python2.7

# Will Fritz
# 12/4/2017

# Uses the composite Simpson rule to approximate the solution to the following integral:
# integral from 0 to 1 of e^x*dx = e - 1
# We also want to determine value of h that guaranteees absolute error is smaller than 10^-10

import math

a = 0.0
b = 1.0

h = 0.1 # arbitrary starting val, will be changed before it is used
absError = float("inf")
exactValue = math.exp(1)-1

# desgribes equation we are taking integral of
def f(x):
    return math.exp(x)

# check a lot of values of n until the abs error is less than 10^-10
for n in range(2, 10000, 2):
    h = (b-a)/n
    xI0 = f(a) + f(b)
    xI1 = 0
    xI2 = 0
    # Use simpsons composite ruls to eventually approximate the integral
    for i in range(1,n):
        x = a + i*h
        if i%2 == 0: #even
            xI2 = xI2 + f(x)
        else:
            xI1 = xI1 + f(x)
    xI = h*(xI0 + 2*xI2 + 4*xI1)/3 # our approximation
    absError = abs(xI - exactValue)
    if absError < 10**-10:
        break

print "The approximation for the integral is: {}".format(xI)
print "The exact value for the integral is: {}".format(exactValue)
print "The h value of {} gave an actual error of: {}".format(h, absError)
