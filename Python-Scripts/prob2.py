# Sum in Loop
# Let us find the sum of several numbers (more than two). It will be useful to
# do this in a loop. As shown in the picture above - you can create variable
# sum and add every value from the list to it. Perhaps "for" loop will suit
# nicely since the amount of numbers is known beforehand.
def sum_nums(numbers):
    result = 0
    for num in numbers:
        result = result + num
    return result

numbers = '804 22 597 705 478 138 563 65 163 988 440 1126 413 419 122 1119 805 540 1185 886 959 1266 1145 193 532 231 786 1298 284 346 552 1078 358 1139 483 827 1268 1037'
num_list = []
for num in numbers.split():
    num_list.append(int(num))
print(sum_nums(num_list))
print(len(num_list))