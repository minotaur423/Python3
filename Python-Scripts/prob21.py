# Array Counters
#
# Here is an array of length M with numbers in the range 1 ... N, where N is less than or equal to 20.
# We are to go through it and count how many times each number is encountered. I.e. it is like Vowel
# Count task, but we need to maintain more than one counter. Be sure to use separate array for them,
# do not create a lot of separate variables, one for each counter.
# Input data contain M and N in the first line.  The second (rather long) line will contain M numbers
# separated by spaces.
# Answer should contain exactly N values, separated by spaces. First should give amount of 1-s, second
# - amount of 2-s and so on.
#
# Example:
#  data input:
#   10 3
#   3 2 1 2 3 1 1 1 1 3
#  Answer:  5 2 3

def count_amt(numbs):
    rng = max(numbs)
    arrays = []
    count = 0
    result = ''
    for i in range(1, rng + 1):
        for n in range(0, len(numbs)):
            if numbs[n] == i:
                count += 1
            else:
                continue
        arrays.append(count)
        count = 0
        result += str(arrays.pop()) + ' '
    return result
  
numbers = '3 20 3 17 19 2 7 7 20 11 16 1 18 20 6 3 7 16 7 16 16 7 9 9 13 18 11 17 1 17 17 4 17 19 20 15 1 6 2 1 17 17 1 14 17 7 17 4 2 3 19 17 10 7 5 2 4 15 19 5 12 15 8 8 14 8 3 14 14 4 14 10 1 15 4 17 1 1 1 3 3 19 19 13 5 4 14 9 19 12 13 11 7 20 19 20 8 1 14 1 5 8 11 5 2 14 2 3 15 2 5 18 20 4 10 5 7 3 14 6 15 6 16 2 6 14 2 13 15 15 13 19 2 3 3 4 17 5 6 12 6 11 9 6 14 18 11 1 1 4 6 16 10 2 17 15 16 18 8 10 12 1 8 14 4 11 17 1 16 2 12 2 13 20 7 6 17 18 6 17 2 12 12 11 14 9 6 9 6 14 18 17 14 6 11 17 17 7 17 12 9 8 13 1 8 20 6 4 18 12 1 19 4 12 10 17 20 16 5 6 9 3 3 2 9 13 19 5 19 16 17 7 4 10 8 11 10 13 14 8 5 15 6 9 6 16 5 6 11 10 12 19 13 14 1 1 7 20 6 5 15 3 12 18 12 19 8 2 12 2 9 17 16 15 5 2 11 9 8 1 19 19 20 11 13 20 11 19 19 17 4 14 19 15 11 11 14 19 13 5 20'
nums = numbers.split()
num_list = []
for j in nums:
    num_list.append(int(j))

print(count_amt(num_list))