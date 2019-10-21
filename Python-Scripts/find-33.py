nums = [3, 1, 3]
for count in range(len(nums) - 1):
    if nums[count] == nums[count+1]:
        result = True
        break
    else:
        result = False
print(result)