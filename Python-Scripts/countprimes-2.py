num = 100
count = 0
nums = []
primes = [2, 3, 5, 7, 11]
for i in range(2,num + 1):
    nums.append(i)
for p in primes:
    for n in nums:
        if n % p == 0 and n != p:
            nums.remove(n)
        else:
            continue
print(len(nums))