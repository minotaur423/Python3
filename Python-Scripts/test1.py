def count_primes(num):
    count = 100
    for i in range(0,num + 1):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0 or i % 11 == 0:
            count -= 1
        else:
            continue
    return (num) - count
result = count_primes(100)
print(result)