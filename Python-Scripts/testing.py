mylist = ['one', 'two', 'three', 'four']
count = len(mylist)
for i in mylist:
    for j in range(count):
        if i != 'two':
            mylist.pop(j)
            count-=1
print(f'This remains of my list: {mylist}')