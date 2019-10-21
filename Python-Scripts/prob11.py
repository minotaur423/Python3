# Sum of digits
# As any number greater than 9 is represented by several digits, we can calculate the sum of these digits.
# For example, for numbers 1492 and 1776 we get:
#  1 + 4 + 9 + 2 = 16
#  1 + 7 + 7 + 6 = 21
# In this task you will be given several numbers and asked to calculate their sums of digits.
# Important: while many programming languages have built-in functions to convert numbers to strings (from
# which digits could be extracted), you should not use this (since your goal is to learn some programming
# tricks).  Instead you need to implement algorithm with repetitive division by 10 (base of numeral system)
# and summing up the remainders. Read the Number to digits article for details on the algorithm.
# Problem statement: 
# Input data are in the following format:
# * first line contains N - the number of values to process;
# * and then N lines will follow describing the values for which sum of digits should be calculated by 3
#   integers A B C;
# * for each case you need to multiply A by B and add C (i.e. A * B + C) - then calculate sum of digits of
#   the result.
# Answer should have N results, also separated by spaces. For example:
#  input data:
#   3
#   11 9 1
#   14 90 232
#   111 15 111
#  answer: 1 16 21
def sum_digits(a,b,c):
    total = (a * b) + c
    total_str = str(total)
    digits = []
    sum_list = []
    for i in range(0,len(total_str)):
        digits.append(total_str[i])
    for j in digits:
        sum_list.append(int(j))
    result = sum(sum_list)
    return result

numbers = '127 242 58 126 281 28 374 185 118 172 206 162 373 23 26 197 273 29 272 272 196 102 220 129 152 145 93 200 297 172 15 87 133 128 177 121 182 157 45'
num_list = numbers.split()
values = []
for num in num_list:
    values.append(int(num))
    
for i in range(0,len(values),3):
    print(sum_digits(values[i],values[i+1],values[i+2]), end=' ')
