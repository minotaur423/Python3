data=([402, 0], [390, 0], [816, 2], [848, 2], [777, 0], [815, 1])
num1 = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num2 = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num3 = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for a, b in data:
    num = list(map(int, str(a)))
    if b == 0:
        num1.remove(num[0])
        num2.remove(num[1])
        num3.remove(num[2])
    else:
        continue
print(int("".join(num1)), int("".join(num2)), int("".join(num3)))