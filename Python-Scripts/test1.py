my_str = 'catcat'
str1 = 'cat'
str2 = 'dog'
ccount = my_str.count('cat')
dcount = 0

for i in range(len(my_str)):
    if str1 in my_str[i:i+3]:
        ccount += 1
    elif str2 in my_str[i:i+3]:
        dcount += 1
    else:
        result = False
if ccount == dcount:
    result = True
else:
    result = False
print(result)