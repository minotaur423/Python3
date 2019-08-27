nums = [1, 6, 2, 2, 7, 1, 6, 99, 99, 7]
nums_list = []
while nums:
    if nums[0] == 6:
        six = nums.index(6)
        seven = nums.index(7)
        for i in range(six,seven+1):
            nums.pop(six)
    else:
        nums_list.append(nums.pop(0))
print(sum(nums_list))