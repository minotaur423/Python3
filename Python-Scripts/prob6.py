# Rounding
# There are several pairs of numbers. For each pair you are to divide first
# by second and return the result, rounded to the nearest integer.
numbers = '5973907 -4197179 17229 562 13563 842 8459140 174 5232395 621 193089 1238875 6927 904 10133 1600 4741639 629 8980745 815 9331 1382 5485 1104 16885 460 9867482 867 2904036 337'
num_list = numbers.split()
length = len(num_list)
i = 0
while i < (length - 1):
    print(round(int(num_list[i]) / int(num_list[i+1])), end=' ')
    i += 2