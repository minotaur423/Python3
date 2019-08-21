mylist = ['one', 'two', 'three', 'four']
count = range(len(mylist))
for i in mylist:
    if i != 'two':
        mylist.pop()
        i-=1
print(f'This remains of my list: {mylist}')