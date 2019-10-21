def LongestWord(sen):
    sen1 = sen.split()
    length = 0
    for word in sen1:
        if len(word) > length:
            length = len(word)
            longestwrd = word
    return longestwrd

print(LongestWord("This is a testing1234 of this function"))
