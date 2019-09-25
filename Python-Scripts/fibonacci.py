# Generate the Fibonacci sequence
def find_fibon(num):
    a = 1
    b = 1
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
