# Generate the Fibonacci sequence
def find_fibon(num):
    primes = []
    while True:
        if num % 2 == 0:
            new_num = num / 2
            primes.append(2)
        elif num % 3 = 
            new_num = num / 3
            primes.append(3)
        
        
    for i in range(num):
        
        yield a
        a, b = b, a+b

#code here
ITERATIONS = 0
while True:
    try:
        ITERATIONS = int(input("Enter the number of fibonacci iterations from five to 20: "))
        if ITERATIONS not in range(5,21):
            continue
    except:
            print("Incorrect entry.  You must enter a number between 5 and 20. Try again.\n")
    else:
        break
    
for num in find_fibon(ITERATIONS):
    print(num)
