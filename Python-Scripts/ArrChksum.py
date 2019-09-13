# Problem 23
def array_chksm(*args):
    result = 0
    value = 113
    modulo = 10000007
    for i in range(len(args)):
        result = (((args[i] + result) * value) % modulo)
    return (result)
 
print(array_chksm(3, 1, 4, 1, 5, 9))