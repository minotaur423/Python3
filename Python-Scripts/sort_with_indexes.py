def sort_idx(data):
    result = []
    swaps = 1
    passes = 0
    swap_total = 0
    orig_data = []
    orig_data.extend(data)
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
    for j in range(len(data)):
        result.append((orig_data.index(data[j]) + 1))
    return result
        
a = [515, 165, 212, 673, 890, 847, 945, 575, 719, 262, 470, 804, 419, 108, 632, 51, 362, 312, 762]
final_result = sort_idx(a)

for u in range(len(a)):
    print(final_result[u], end=" ")