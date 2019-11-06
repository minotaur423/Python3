def calc_savings(s, r, p):
    new_s = 0.0
    for y in range(30):
        new_s += (s * (p/100) + s)
        if new_s == r:
            break
        else:
            continue
    return y

data=([1000, 10000, 8], [50, 100, 25])

for a,b,c in data:
    print(calc_savings(a,b,c), end=" ")