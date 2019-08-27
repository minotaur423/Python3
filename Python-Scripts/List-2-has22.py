nums = [2]
result = False
for i in range(len(nums)-1):
    if nums[i] == 2 and nums[i+1] == 2:
        result = True
        break
print(result)