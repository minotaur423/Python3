nums = [5, 13, 2]
nums_list = []
while nums:
    if nums[0] == 13:
        nums.remove(nums[0])
        if len(nums) > 0:
            nums.pop(0)
        else:
            break
    else:
        nums_list.append(nums.pop(0))
print(sum(nums_list))