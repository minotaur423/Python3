# Generate the Fibonacci sequence
def find_primes(num):
    primes = []
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
            primes.append(i)
        else:
            continue
    return count
        
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
