# Average of an array
# Average (or mean) value of some numbers could be calculated as their sum divided by
# their amount. For example:
#  avg(2, 3, 7) = (2 + 3 + 7) / 3 = 4
#  avg(20, 10) = (20 + 10) / 2 = 15
# You will be given several arrays, for each of which you are to find an average value.
# Input data will give the number of test-cases in the first line. Then test-cases
# themselves will follow, one case per line. Each test-case describes an array of
# positive integers with value of 0 marking end. (this zero should not be included
# into calculations!!!).
# Answer should contain average values for each array, rounded to nearest integer
# (see task on rounding), separated by spaces.
# Example:
#  input data:
#   3
#   2 3 7 0
#   20 10 0
#   1 0
# Answer:  4 15 1
def avg_nums(nums):
    count = 0
    sum_num = 0
    count = 0
    for arg in nums:
        if arg != 0:
            sum_num += arg
            count += 1
    result = round(sum_num / count)
    return result

numbers = ['6445 5437 6396 14805 7404 4662 16232 15918 0', '5252 14707 3760 5533 13765 1377 6422 0', '1676 394 1579 1438 1903 1580 1454 1766 1035 1356 0', '57 480 774 982 942 41 0', '3674 13302 3470 1996 677 9003 15761 2054 15425 7543 9337 12446 10690 5580 7561 0', '44 114 158 214 149 252 228 13 189 217 248 0', '7034 2 4981 576 1000 5320 5078 689 6347 4598 4460 2823 2628 0', '3205 3188 3265 3906 910 1695 3222 0', '691 870 135 534 836 930 325 692 930 948 764 31 589 0', '90 238 169 178 64 219 98 8 163 0', '14010 9659 12601 10759 16131 7267 0', '247 83 6 73 256 239 54 191 246 201 0', '34 9 188 212 72 151 0', '226 390 300 78 994 64 750 0']
values: list = []
final_result = 0
for i in numbers:
    num = i.split()
    del values[::]
    for j in num:
        values.append(int(j))
    final_result = avg_nums(values)
    print(final_result, end=' ')