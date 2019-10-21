# Array Checksum
# Problem statement
# You will be given the array for which checksum should be calculated. Perform calculation as
# follows: for each element of the array (starting from beginning) add this element to result
# variable and multiply this sum by 113 - this new value taken by modulo 10000007 should become
# the next value of result, and so on.
#  Read the article on checksum for detailed description of this algorithm. An example of
# calculation also could be found there.
# Input data will tell the length of an array in the first line. Array values themselves follow
# in the second line, separated by spaces.
# Answer should have a single value - calculated checksum.
# Example:
#  input data:
#   6
#   3 1 4 1 5 9
#  answer: 8921379
# All input values are between 0 and 1,000,000,000 - be sure to take care of possible overflow
# in progress of calculations!

def checksum_value(digits):
    result = 0
    for digit in digits:
        result += digit
        result = result * 113
        result = result % 10000007
    return result

numbers = '289 22584886 807675553 57658507 994 0 476172 32604 3987 65301220 253 4416060 61 84255286 67786 7284986 564553980 897965254 8697 653904267 5036479 4529279 33516 95670 3018644 96501 370 50305 368101475'
nums_list = numbers.split()
values = []

for num in nums_list:
    values.append(int(num))
    
print(checksum_value(values))