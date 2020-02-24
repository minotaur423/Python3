def summer_69(arr):
    new_arr = []
    for num in arr:
        if num not in range(6,10):
            new_arr.append(num)
        else:
            continue
    return sum(new_arr)

print(summer_69([2, 1, 6, 9, 11]))