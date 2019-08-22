mylist = ['one', 'two', 'three', 'four']
for i in range(len(mylist)):
    for j in mylist[i]:
        if j == 'two':
            continue
        else:
            mylist.pop(i)
print(f'This remains of my list: {mylist}')