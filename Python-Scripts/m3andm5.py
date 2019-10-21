nums = range(1000)
new_nums = 0
for i in nums:
    if i % 3 == 0 or i % 5 == 0:
        new_nums += i
print(new_nums)