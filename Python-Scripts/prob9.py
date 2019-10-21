# Triangles
# You are given several triplets of values representing lengths of the
# sides of triangles. You should tell from which triplets it is possible
# to build triangle and for which it is not.
# Input data: A number of triplets.
# Other lines will contain triplets themselves (each in separate line).
# Answer: You should output 1 or 0 for each triplet (1 if triangle
# could be built and 0 otherwise).
def check_triangle(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return 1
    return 0

int_list = []
side_lengths = '616 1553 805 766 1492 1456 181 203 305 1915 926 1380 493 852 1974 510 197 223 1800 840 890 592 1108 700 384 1513 636 1386 1523 882 1713 751 480 615 1759 866 155 194 473 500 645 1497 709 1439 815 407 261 178 550 1072 867 2038 740 1427 383 737 262 606 1057 383 780 416 1440 838 430 2014 575 714 1441 599 837 1496 1272 897 916 940 517 1984 312 238 727 537 455 420 301 548 605 1020 2404 700'
side_list = side_lengths.split(' ')
for side in side_list:
    int_list += [int(side)]

for i in range(0,len(side_list),3):
    print(check_triangle(int_list[i],int_list[i+1],int_list[i+2]), end=' ')