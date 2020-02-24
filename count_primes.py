def count_primes(num):
    nums = [2,3]
    for i in range(4, num + 1):
        for j in 2, 3, 5, 7, 9, 11, 13:
            if i % j == 0 and i >= j:
                break
            else:
                nums.append(i)
    return len(nums)

print(count_primes(100))