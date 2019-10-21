# Arithmetic Progression
# You are to calculate the sum of first members of arithmetic sequence.
# Input data: first line contains the number of test-cases.  Other lines
# contain test-cases in form of triplets of values A B N where A is the first
# value of the sequence, B is the step size and N is the number of first values
# which should be accounted.
# Answer: you are to output results (sums of N first members) for each sequence,
# separated by spaces.
def sum_progression(a,b,n):
    result_list = []
    result_list.append(a)
    for i in range(1,n):
        a += b
        result_list.append(a)
    return sum(result_list)

values = '8 13 99 20 19 18 24 7 84 15 8 96 20 12 19 16 13 38 23 11 74 10 16 48'
values_list = values.split(' ')
total = 0
int_list = []
for value in values_list:
    int_list += [int(value)]
for i in range(0,len(int_list),3):
    total = sum_progression(int_list[i],int_list[i+1],int_list[i+2])
    print(total, end=' ')