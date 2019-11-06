import math
def calc_savings(s, r, p):
    new_s = s
    y = 0
    while True:
        new_s += (math.floor(new_s) * (p/100))
        if new_s > r:
            y += 1
            break
        else:
            y += 1
            continue
    return y

data=([50, 750, 7], [25, 475, 25], [5000, 70000, 35], [500, 8500, 3], [500, 9000, 1], [500, 4000, 35], [100, 2000, 25], [1000, 5000, 50], [1000, 12000, 7], [25, 375, 50], [250, 750, 1], [250, 750, 7], [100, 800, 40], [2500, 12500, 25], [250, 1250, 7], [2500, 17500, 5], [100, 500, 10])

for a,b,c in data:
    print(calc_savings(a,b,c), end=" ")