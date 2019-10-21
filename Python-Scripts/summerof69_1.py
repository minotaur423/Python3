arr = [2, 1, 6, 9, 11] # type: list
total = 0
six = 0
nine = 0
for count in range(len(arr)):
    if arr[count] == 6:
        six = count
    elif arr[count] == 9:
        nine = count
    else:
        continue
if 6 in arr:
    total = sum(arr) - sum(arr[six:nine+1])
else:
    total = sum(arr)
print(total)