def josephus_prb(N, K):
    count = 0
    num_list = list(range(1, N + 1))
    result = 0
    rounds = 0
    while len(num_list) > 1:
        i = 0
        rounds += 1
        while i < len(num_list):
            count += 1
            if count % K == 0:
                num_list.pop(i)
            else:
                i += 1
                continue
    result = num_list[0]
    return result

data = (99, 25)
a, b = data

print(josephus_prb(a, b), end=" ")