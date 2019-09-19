# Here is one of the earliest methods for producing sequence of seemingly independed (i.e. pseudorandom) numbers:

# 1. Choose some initial value with 4 digits (i.e. in range 0000 ... 9999).
# 2. Multiply it by itself (i.e. raise to power 2) to get value consisting of 8 digits (add leading zeroes if necessary).
# 3. Truncate two first and two last digits in decimal representation of this result.
# 4. New value will contain 4 digits and it is the next value of a sequence.
# 5. To get more values, repeat from step 2.

def randgen(num):
    iterations = 1
    num_list = []
    squared_num = 0
    new_num = num
    while True:
        num_list.append(new_num)
        squared_num = new_num**2
        new_num = int((squared_num / 100) % 10000)
        if new_num in num_list:
            break
        else:
            iterations += 1
    return iterations

for i in (405, 9251, 3779, 1451, 7589, 6212, 3761, 7849, 3488, 1532, 8096, 6068):
    print(randgen(i), end=" ")