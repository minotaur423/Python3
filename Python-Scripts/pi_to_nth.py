# Find PI to the Nth Digit
import math
def find_pi(num):
    return round(math.pi, num)

#code here

while True:
    try:
        DECIMAL_PLACE = int(input("Enter a number from 1 to ten: "))
    except:
        print("Incorrect entry.  You must enter a number between 1 and 10. Try again.\n")
    else:
        break

print(find_pi(DECIMAL_PLACE))
