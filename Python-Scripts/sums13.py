nums = [13, 1, 13]
new_sum = 0
length = len(nums)
i = 0
while i < length:
    if nums[i] == 13:
        del nums[i:i+2]
        length = len(nums)
    else:
        i += 1
new_sum = sum(nums)
print(new_sum)