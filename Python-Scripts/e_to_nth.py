# Generate the Fibonacci sequence
def find_e(num):
    for i in range(num):
        
    return round(math.e, num)

#code here

while True:
    try:
        DECIMAL_PLACE = int(input("Enter a number from 1 to ten: "))
    except:
        print("Incorrect entry.  You must enter a number between 1 and 10. Try again.\n")
    else:
        break

print(find_e(DECIMAL_PLACE))
