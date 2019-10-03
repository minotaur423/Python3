def gcd(a, b):
    gcd = 0
    for i in range(max(a, b)):
        if a < b:
            b = b - a
        elif b < a:
            a = a - b
        elif a == b:
            gcd = a
            break
    return gcd

#def lcm(a,b):
#    a * b / gcd(a, b)
print("Please enter two numbers to get the Greatest Common Denominator.\n")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(f'\nThe Greatest Common Denominator for {a} and {b} is {gcd(a, b)}.')