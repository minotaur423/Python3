def print_time(x,y,n):
    count_s = 0
    count_l = 0
    largest = 0
    smallest = 0
    time_s = 0
    result = 0
    if x < y:
        largest = y
        smallest = x
    else:
        largest = x
        smallest = y
    time_l = largest
    for j in range(smallest, n * largest, smallest):
        if count_l + count_s >= n:
            break
        else:
            count_s += 1
            if j > time_l:
                time_l += largest
                count_l += 1
    time_s = smallest * count_s
    return time_s

data = [ 2938, 17117, 35257, \
         21, 18, 26371539, \
         8, 4, 56516287, \
         1482435, 652725, 663, \
         3, 5, 76220966, \
         33651989, 47378383, 16, \
         1, 1, 919346302, \
         32021286, 62505152, 10, \
         38089992, 145006872, 6, \
         45, 68, 7862163, \
         98939, 86910, 7670, \
         13394, 28894, 7418, \
         18348, 23198, 28641, \
         658051, 548411, 642, \
         1, 1, 675388538, \
         1621, 1678, 390004, \
         6, 6, 86050017, \
         42, 1136, 878245 ]

for i in range(0,len(data),3):
    print(print_time(data[i],data[i+1],data[i+2]), end=' ')