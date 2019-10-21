s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
ucase = 0
lcase = 0
for l in s:
    if l.isupper():
        ucase += 1
    elif l.islower():
        lcase += 1
    else:
        continue
print(f'No. of Upper case Characters : {ucase}')
print(f'No. of Lower case Characters : {lcase}')