nums = [1, 2, 3, 4, 100]
max_num = max(nums)
min_num = min(nums)
nums.remove(max_num)
nums.remove(min_num)
sum_num = 0
count = 0
for num in nums:
    sum_num += num
    count += 1
print(int(sum_num/count))