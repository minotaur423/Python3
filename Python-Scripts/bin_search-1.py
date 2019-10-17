data = ([0.59912051, 0.64030348, 263.33721367, 387.92069617], [15.68387514, 1.26222280, 695.23706506, 698.72384731])
from math import sqrt,exp
from decimal import *
from numpy import arange

x = 0.0
for a, b, c, d in data:
    for x in arange(0.000000001, 1000, 0.00001):
        result = a * x + b * sqrt(x**3) - c * (exp(-x/50)) - d
        if result >= 0:
            break
        x += 1
    getcontext().prec = 12
    print(x, end=" ")
    
print("Float range using NumPy arange():")

print("\nTest 1:")
for i in arange(0.0, 1.0, 0.1):
    print(i, end=', ')

print("\n\nTest 2:")
for i in arange(0.5, 5.5, 0.5):
    print(i, end=', ')

print("\n\nTest 3:")
for i in arange(-1.0, 1.0, 0.5):
    print(i, end=', ')