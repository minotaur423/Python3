# Generate the Fibonacci sequence
def find_primes(num):
    primes = []
    non_primes = []
    for i in range(2, num + 1):
        if i % 2 == 0 and i > 2:
            non_primes.append(i)
        elif i % 3 == 0 and i > 3:
            non_primes.append(i)
        elif i % 5 == 0 and i > 5:
            non_primes.append(i)
        elif i % 7 == 0 and i > 7:
            non_primes.append(i)
        elif i % 11 == 0 and i > 11:
            non_primes.append(i)
        else:
            primes.append(i)
    return primes

        
#code here
NUMBER = iter(find_primes(1000))
print(f'The first prime number is {next(NUMBER)}.\n')

# print(f'The prime numbers are: {find_primes(number)}')
while True:
    try:
        CONTINUE = input("Would you like to see the next prime number? (Y/n): ")
        if CONTINUE.lower() == 'y':
            print(f'The next prime number is {next(NUMBER)}.')
            continue
        elif CONTINUE.lower() == 'n':
            print("Exiting")
            break
    except:
        print("Incorrect entry.  You must enter Y or n.\n")
        continue
    else:
        break