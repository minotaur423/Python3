# Square Root
# Refer to Square Root Approximation article for more details on the Heron's Method.
# So we are given values X for which to perform calculations and number of steps N to perform.
# Use r = 1 at the beginning, and output resulting approximation (after N steps).
# Input data will give the number of test-cases in first line.
# Next lines will contain test-cases themselves, each containing the value X for which square
# root should be calculated and N - the number of calculation steps.
# Answer should contain calculated approximations for each case, separated by space.
# Example:
#  input data:
#   3
#   150 0
#   5 1
#   10 3
#  Answer:  1 3 3.196
def sqr_root(num, step):
    r = 1.0
    d = 0.0
    result = 0.0
    count = 0
    while step > count:
        d = num / r
        result = abs(r - d)
        if result > 0.0:
            r = (r + d) / 2
        else:
            break
        count += 1
    return r

numbers = '31419 3 45 2 825 3 4055 9 49191 7 4771 2 4273 1 510 13 4596 4 39758 6 224 11'
nums_list = numbers.split()
values = []
steps = []
result = 0.0
for i in range(len(nums_list)):
    if i % 2 == 0:
        values.append(int(nums_list[i]))
    else:
        steps.append(int(nums_list[i]))
for j in range(len(values)):
    result = sqr_root(values[j],steps[j])
    print(format(result, '.12g'), end=' ')