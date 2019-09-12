# Problem 22
def two_prnt(x,y,n):
    time = 0
    if x < y:
        faster = x
        slower = y
    else:
        faster = y
        slower = x
    difference = slower - faster
    for i in range(1, n+1, faster):
        time += x*n + y*n)
    time = time/n
    return time

print(two_prnt(3, 5, 4), end=" ")