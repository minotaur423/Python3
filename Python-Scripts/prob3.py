# Sums in Loop
# Now we are given several pairs of values and we want to calculate sum for
# each pair.
numbers = '470909 982210 775900 323643 300994 75970 640859 598818 779692 487081 797972 115123 622522 532037 233558 689138 224497 661310 743714 838640 168574 133307 920694 472924 449040 249851'
num_list = numbers.split()
length = len(num_list)
even_nums = slice(0,length,2)
odd_nums = slice(1,length,2)
even_list = num_list[even_nums]
odd_list = num_list[odd_nums]
for i in range(len(even_list)):
    print(int(even_list[i]) + int(odd_list[i]), end=' ')
