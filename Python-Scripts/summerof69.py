arr = [2, 1, 6, 9, 11] # type: list
count = 0
total = 0
six = 0
nine = 0
for num in arr:
    if num == 6:
        six = count
        count += 1
    elif num == 9:
        nine = count
        count += 1
    else:
        count += 1
if 6 in arr:
    total = sum(arr) - sum(arr[six:nine+1])
else:
    total = sum(arr)
print(total)