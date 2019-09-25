# Find PI to the Nth Digit
import math
def find_pi(n):
    return round(math.pi,n)

#code here

while True:
    try:
        decimal_place = int(input("Enter a number from 1 to ten: "))
    except:
        print("Incorrect entry.  You must enter a number between 1 and 10. Try again.\n")
    else:
        break

print(find_pi(decimal_place))
