def bmi(w, h):
    result = w / h**2
    if result < 18.5:
        return "under"
    elif result > 18.5 and result < 25.1:
        return "normal"
    elif result > 25.0 and result < 30.0:
        return "over"
    else:
        return "obese"
        
data = ([103, 1.77], [43, 1.64], [97, 2.84], [97, 2.54], [47, 1.13], [42, 1.07], [82, 1.85], [77, 2.53], [91, 1.91], [66, 1.37], [71, 1.54], [59, 1.32], [111, 1.92], [56, 1.67], [112, 1.74], [85, 1.71], [107, 1.99], [112, 2.12], [93, 1.86], [97, 1.77], [88, 1.68], [99, 2.66], [59, 1.92], [53, 1.25], [98, 2.02], [103, 2.71], [57, 2.28])
for weight, height in data:
    print(bmi(weight, height), end=" ")