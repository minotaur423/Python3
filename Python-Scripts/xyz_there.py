str1 = 'abc.xyzxyz'
result = bool

if 'xyz' in str1 and '.xyz' not in str1:
    result = True
elif 'xyz' not in str1:
    result = False
else:
    for i in range(len(str1)-3):
        if str1[i:i+4] == '.xyz':
            result = False
        else:
            result = True
print(result)