# Linear Function
# Linear function is defined by an equation: y(x) = ax + b
# Slope: y2 - y1 / x2 - x1
# B-Intercept: y1 - (slope * x1)
# You are told two pairs of values (x1, y1), (x2, y2) which satisfy the
# function equation - and you should restore the equation itself.
# Input data has test-cases themselves in separate lines. Each case
# contains 4 integers # (x1 y1 x2 y2).
# Answers should be integer too and you are to write them in line,
# separating with spaces and enclosing each pair in parenthesis, for
# Example:
# input data:
#  2
#  0 0 1 1
#  1 0 0 1
#
# answer: (1 0) (-1 1)
def check_coords(x1,y1,x2,y2):
    slope = int((y2 - y1) / (x2 - x1))
    bintercept = int(y1 - (slope * x1))
    result = f'({slope} {bintercept})'
    return result

int_list = []
coordinates = '-749 -67996 199 17324 -768 20324 299 -7418 -919 279 -122 279 305 -17116 873 -47220 110 1131 168 1247 405 -15586 -158 5245 558 -26445 618 -29385 -66 -3777 554 36523 -246 -22447 -335 -30635 964 -44359 541 -24901 -581 41458 -271 18828 -398 36543 114 -9537 -717 -44459 -739 -45845'
coord_list = coordinates.split(' ')
for coord in coord_list:
    int_list += [int(coord)]

for i in range(0,len(int_list),4):
    print(check_coords(int_list[i],int_list[i+1],int_list[i+2],int_list[i+3]), end=' ')