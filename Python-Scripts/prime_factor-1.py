# Generate the Fibonacci sequence
def find_primes(num):
    primes = []
    while num % 2 == 0:
        num = int(num / 2)
        primes.append(2)
        
    while num % 3 == 0:
        num = int(num / 3)
        primes.append(3)
        
    while num % 5 == 0:
        num = int(num / 5)
        primes.append(5)

    for i in range(3,num,2):
        if num % i == 0:
            num = int(num / i)
            primes.append(i)
        else:
            continue
    if num > 1:
        primes.append(num)
    return sorted(primes)
        
#code here
NUMBER = 0
while True:
    try:
        NUMBER = int(input("Enter a number from 2 to 1000 to get the number of factors it has: "))
        if NUMBER not in range(2, 1001):
            continue
    except:
        print("Incorrect entry.  You must enter a number between 2 and 1000. Try again.\n")
    else:
        break
for number in range(2, NUMBER):
    print(f'The number of primes in {number} is {find_primes(number)}.')
