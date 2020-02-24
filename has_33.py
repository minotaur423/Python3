def has_33(nums):
    index = len(nums) - 1
    result = False
    for i in range(index):
        if nums[i] == 3:
            if nums[i + 1] == 3:
                result = True
        else:
            continue
    return result

print(has_33([1, 3, 1, 3]))