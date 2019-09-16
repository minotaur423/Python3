def palindrome(s):
    first_part = []
    last_part = []
    count = 0
    reverse = (len(s) -1)
    mid_point = int(len(s)/2)
    while count < mid_point:
        first_part.append(s[count])
        last_part.append(s[reverse])
        count += 1
        reverse -= 1
    if first_part == last_part:
        return True
    else:
        return False

print(palindrome('helleh'))