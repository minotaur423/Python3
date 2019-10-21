nums = [1,2,4,0,0,7,5]
code = [0,0,7,'x']
for num in nums:
    if num == code[0]:
        code.pop(0)
print(len(code) == 1)