# Problem 22
def two_prnt(x,y,n):
    time = 0
    pages = 0
    f_time = 0
    s_time = 0
    faster = 0
    slower = 0
    max_time = 0
    if x < y:
        faster = x
        slower = y
        max_time = slower * n
    elif y < x:
        faster = y
        slower = x
        max_time = slower * n
    else:
        slower = x
        faster = y
        max_time = (slower + 1) * n
    for i in range(1, max_time):
        if pages >= n:
            time = max(f_time,s_time)
            break
        else:
            if i % faster == 0:
                pages += 1
                f_time += faster
            if i % slower == 0:
                pages += 1
                s_time += slower
    return time

grps = ([105684995, 96944250, 8], [12, 88, 10647638], [1, 1, 927175744], [4979224, 7901223, 94], [388996, 376949, 772], [90334, 23099, 5050], [705, 2744, 294119], [68, 3504, 215562], [6, 8, 85993693], [1, 1, 658189901], [760, 995, 749854], [1288, 2455, 379320], [3, 2, 78874497], [407746, 1383237, 680], [2, 2, 484393235], [52, 73, 7621777])
for a,b,c in grps:
    print(two_prnt(a,b,c), end=" ")