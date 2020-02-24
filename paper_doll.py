def paper_doll(text):
    new_string = ''
    for i in range(len(text)):
        new_string += text[i] * 3
    return new_string

print(paper_doll('Hello'))