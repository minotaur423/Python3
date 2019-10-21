nums = [13, 1, 2, 13, 2, 1, 13]
new_sum = 0
for i, v in enumerate(nums):
    if v == 13 and i < len(nums):
        del nums[i:i+2]
new_sum = sum(nums)
print(new_sum)