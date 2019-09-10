data = (3, 1, 4, 1, 5, 9)
modulo = 10000007
multiplier = 113
result = 0
for i in data:
    result = (result + i) * multiplier
print(result  % modulo)