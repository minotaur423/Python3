def calc_savings(s, r, p):
    new_s = s
    for y in range(1,31):
        new_s += (new_s * (p/100))
        if new_s >= r:
            break
        else:
            continue
    return y

data=([1000, 10000, 8], [50, 100, 25])

for a,b,c in data:
    print(calc_savings(a,b,c), end=" ")