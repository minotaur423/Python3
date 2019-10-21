str = 'Anthropomorphism'
new_str = ''
i = 0
for letter in str:
    if i % 2 == 0:
        new_str += letter.upper()
    else:
        new_str += letter
    i += 1
print(new_str)