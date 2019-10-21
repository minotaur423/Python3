# Weighted sum of digits
# Let us calculate sum of digits, as earlier, but multiplying each digit by its position (counting from the left,
# starting from 1). For example, given the value 1776 we calculate such weighted sum of digits (let us call it
# "wsd") as: wsd(1776) = 1 * 1 + 7 * 2 + 7 * 3 + 6 * 4 = 60
# Input data will give the number of test-cases in the first line. Values themselves are in the second line.
# For each of these values you are to calculate weighted sum of digits.
# Answer: as usually, put results in one line, separating them with spaces.
# Example:
#  input data:
#   3
#   9 15 1776
#  answer: 9 11 60

def process_num(a):
    split = str(a)
    count = 1
    result = 0
    for i in range(len(split)):
        subtotal = int(split[i]) * count
        count += 1
        result += subtotal
    return result
        
numbers = '16807220 1443374 4951 371 2 12479910 26771 358433 11327 4 49993030 49 16 2 106266 13864312 1337763 4738 3078226 47122 10 10 24 294155033 1313 334723 30532 2160 62114131 972344 66593635 70326838 10 1777346 1 52884 21544'
num_list = numbers.split()
values = []

for num in num_list:
    values.append(int(num))

for num in values:
    print(process_num(num), end=' ')