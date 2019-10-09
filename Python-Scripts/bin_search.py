def bin_search(A, B, C, D):
    from math import sqrt
    from math import e
    # Define variables
    result = 0.0
    for x in range(1, 1000):
        result = (A * x) + (B * sqrt(x**3)) + (-C * ((e/x)**(1/50))) + -D
        if result in range(0, 1):
            
            return round(x, 12)

data = ([0.59912051, 0.64030348, 263.33721367, 387.92069617], [15.68387514, 1.26222280, 695.23706506, 698.72384731])
for a, b, c, d in data:
    print(bin_search(a, b, c, d), end=" ")