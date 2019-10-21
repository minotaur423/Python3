nums = [1,0,2,4,0,5,7]
result = bool()
if 0 in nums:
    first = nums.index(0)
if 0 in nums[first + 1:]:
    second = nums.index(0,first + 1)
if 7 in nums[second + 1:]:
    third = nums.index(7,second + 1)
    result = True
print(result)