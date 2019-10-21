num = 100
count = 0
nums2 = []
nums3 = []
nums5 = []
nums7 = []
nums11 = []
# primes = [2, 3, 5, 7, 11]
for i in range(2,num+1):
    if i % 2 != 0 and i != 2:
        nums2.append(i)
    else:
        continue
for i in nums2:
    if i % 3 != 0 and i != 3:
        nums3.append(i)
    else:
        continue
for i in nums3:
    if i % 5 != 0 and i != 5:
        nums5.append(i)
    else:
        continue
for i in nums5:
    if i % 7 != 0 and i != 7:
        nums7.append(i)
    else:
        continue
for i in nums7:
    if i % 11 != 0 and i != 11:
        nums11.append(i)
    else:
        continue
print(len(nums11) + 5)