data = ([0.59912051, 0.64030348, 263.33721367, 387.92069617], [15.68387514, 1.26222280, 695.23706506, 698.72384731])
from math import sqrt,exp

x = 0.00000001
for a, b, c, d in data:
    x = 0.00000001
    while True:
        x += 0.0000000001
        result = a * x + b * sqrt(x**3) - c * (exp(-x/50)) - d
        if result >= 0:
            break
    print(round(x, 12), end=" ")