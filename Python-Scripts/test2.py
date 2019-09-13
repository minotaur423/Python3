# Problem 23
def array_chksm(args):
    result = 0
    value = 113
    modulo = 10000007
    for i in range(len(args)):
        result = (((args[i] + result) * value) % modulo)
    return (result)
 
data = [1, 4, 3, 2, 6, 5, -1]
for i in range(len(data)-1):
    if data[i] > data[i+1] and data[i+1] != -1:
        data[i], data[i+1] = data[i+1], data[i]
    else:
        continue
data.pop()
print(array_chksm(data))