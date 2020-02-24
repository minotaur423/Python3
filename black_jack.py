def blackjack(a,b,c):
    if a + b + c <= 21:
        result = a + b + c
    elif (a + b + c) > 21 and a == 11 or b == 11 or c == 11:
        if ((a + b + c) - 10) > 21:
            result = str('BUST')
        else:
            result = (a + b + c) - 10
    else:
        result = str('BUST')
    return result

print(blackjack(9,9,11))