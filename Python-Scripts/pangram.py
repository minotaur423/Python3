import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
#    result = False
#    for letter in str1.lower():
#        if letter in alphabet:
#            alphabet = alphabet.replace(letter,"")
#    if alphabet == "":
#        result = True
#    return print(result)
    return print(alphaset <= set(str1.lower()))

ispangram("The quick brown fox jumps over the lazy dog")