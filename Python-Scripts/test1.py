def weighted_digits(*args):
    result = 0
    str_num = " "
    for arg in args:
        str_num = str(arg)
        list_num = str_num.split()
        for i in range(0, (len(list_num))):
            result += (int(list_num[i]) * i + 1)
    return result

for i in [9, 15, 1776]:
    print(weighted_digits(i), end=" ")