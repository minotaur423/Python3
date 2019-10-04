def bubble_sort(data):
    swaps = 1
    passes = 0
    swap_total = 0
    n1 = 0
    n2 = 1
    while swaps:
        n1 = 0
        n2 = 1
        swaps = 0
        for i in range(len(data) - 1):
            if data[n1] <= data[n2]:
                pass
            else:
                data[n1], data[n2] = data[n2], data[n1]
                swaps += 1
            n1 += 1
            n2 += 1
        swap_total += swaps
        passes += 1
    result = (f'{passes} {swap_total}')  
    return result
        
a = [6, 16, 9, 12, 17, 1, 3, 2, 14, 13, 8, 4, 5, 11, 10, 15, 7]
print(f'{bubble_sort(a)}')