def josephus_prb(N, K):
    count = 0
    num_list = list(range(1, N + 1))
    result_list = []
    result_list.extend(num_list)
    while len(num_list) > 1:
        for i in range(1, K + 1):
            num_list.pop(num_list.index(3 * i))
        else:
            continue
    result = num_list
    return result

data = (10, 3)
a, b = data

print(josephus_prb(a, b), end=" ")