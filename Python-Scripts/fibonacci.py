nums = 34
total = 0
num1 = 0
num2 = 1
count = 0
sum_even = 0
for count in range(nums):
    if total < 4000000:
        total = num1 + num2
        if total % 2 == 0:
            sum_even += total
        num1 = num2
        num2 = total
        count += 1
    else:
        break
print(sum_even)
