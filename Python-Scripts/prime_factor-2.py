# Generate the Fibonacci sequence
def find_primes(num):
    primes = []
    while num % 2 == 0:
        num = int(num / 2)
        primes.append(2)
    
    for i in range(3,num**2):
        if num % i == 0:
            num = num / i
            primes.append(2)
        elif num % 3 == 0:
            num = num / 3
            primes.append(3)
        elif num % 5 == 0:
            num = num / 5
            primes.append(5)
        elif num % 7 == 0:
            num = num / 7
            primes.append(7)
        else:
            continue
    return primes
        
#code here
NUMBER = 0
while True:
    try:
        NUMBER = int(input("Enter a number from 2 to 200 to get the number of factors it has: "))
        if NUMBER not in range(2,201):
            continue
    except:
        print("Incorrect entry.  You must enter a number between 2 and 200. Try again.\n")
    else:
        break
    
print(f'The number of primes in {NUMBER} is {find_primes(NUMBER)}.')
