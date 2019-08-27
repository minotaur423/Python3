n = 11
outside_mode = True

result = bool
if n in range(1,11) and outside_mode == True:
    if n <= 1 or n >= 10:
        result = True
    else:
        result = False
elif n not in range(1,11) and outside_mode == False:
    result = False
else:
    result = True
    
print(result)