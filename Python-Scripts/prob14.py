# Modular Calculator
# Input data will have:
#  * initial integer number in the first line;
#  * one or more lines describing operations, in form sign value where sign is
#    either + or * and value is an integer;
#  * last line in the same form, but with sign % instead and number by which the
#    result should be divided to get the remainder.
# Answer should give remainder of the result of all operations applied sequentially
# (starting with initial number) divided by the last number.
# Example:
#  input data:
#   5
#   + 3
#   * 7
#   + 10
#   * 2
#   * 3
#   + 1
#   % 11
# answer:  1
# In this case result after all operations applied sequentially is 397.  All numbers
# will not exceed 10000 (though intermediate results could be very large).

numbers = '* 6 * 740 + 21 * 68 * 6 * 8 * 243 + 10 * 3429 + 979 * 317 * 895 * 337 * 7 * 46 + 691 * 3008 * 98 * 74 + 67 + 19 + 789 * 4193 + 6 * 86 + 46 * 5 * 8 + 1 * 555 + 9 * 5914 + 462 * 686 * 95 + 23 * 33 + 47 + 68 + 29 * 396 * 33 * 9699 * 663 * 1 * 48 + 8 * 10 % 7794'
operands = ['+', '*', '/', '-', '%']
num_list = numbers.split()
values = [591]
action = []
result = 591
num = 0
for i in num_list:
    if i in operands:
        action.append(i)
    else:
        values.append(int(i))

for j in range(len(values)-1):
    if action[j] == '+':
        result = result + values[j+1]
    elif action[j] == '*':
        result = result * values[j+1]
    else:
        result = result % values[-1]

print(result, end=' ')