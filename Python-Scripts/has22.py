nums = [1, 2, 2]
result = bool()
for i in range(len(nums)-1):
    if nums[i] == 2 and nums[i+1] == 2:
        result = True
    else:
        result = False
print(result)