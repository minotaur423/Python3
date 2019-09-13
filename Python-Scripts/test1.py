# Problem 23
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    for i in alphabet:
        if i in str1.lower():
            result = True
        else:
            result = False
            break
    return result

print(ispangram("The quick brown fox jumps over lazy dog"))