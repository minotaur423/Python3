# Here is one of the earliest methods for producing sequence of seemingly independed (i.e. pseudorandom) numbers:

# 1. Choose some initial value with 4 digits (i.e. in range 0000 ... 9999).
# 2. Multiply it by itself (i.e. raise to power 2) to get value consisting of 8 digits (add leading zeroes if necessary).
# 3. Truncate two first and two last digits in decimal representation of this result.
# 4. New value will contain 4 digits and it is the next value of a sequence.
# 5. To get more values, repeat from step 2.

def randgen(num):
    new_num = num**2
    str_num = str(new_num)
    if len(str_num) % 2 == 0:
        middle = int(len(str_num) / 2)
        mid_num = str_num[middle]