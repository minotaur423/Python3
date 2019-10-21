def make_chocolate(small, big, goal):
    bb_amt = goal / (big * 5)
    if bb_amt >= big:
        return goal - (big * 5)
    else:
        return goal % 5
    if (bb_amt * 5) + small >= goal:
        return goal - (bb_amt * 5)
    elif (bb_amt * 5) + small < goal:
        return -1
    else:
        return 123

print(f'make_chocolate(4, 1, 10) = {make_chocolate(4, 1, 10)}')
print(f'make_chocolate(4, 1, 9) = {make_chocolate(4, 1, 9)}')
print(f'make_chocolate(5, 4, 9) = {make_chocolate(5, 4, 9)}')
