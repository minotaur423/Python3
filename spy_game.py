def spy_game(nums):
    result = False
    spy = []
    for num in nums:
        if num == 0 or num == 7:
            spy.append(num)
        else:
            continue
        if spy == [0, 0, 7]:
            result = True
    return result

print(spy_game([1,7,2,0,4,5,0]))