a = 9
b = 9
c = 9
if a + b + c <= 21:
    print(a + b + c)
elif a == 11 or b == 11 or c == 11 and a + b + c - 10 <= 21:
    print((a + b + c) - 10)
else:
    print('BUST')