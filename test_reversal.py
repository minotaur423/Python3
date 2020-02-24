def master_yoda(text):
    words = text.split()
    new_words = ""
    index = len(words) - 1
    while -1 < index:
        new_words += " ".join([words[index]])
        new_words += " "
        index -= 1
    print(new_words)

master_yoda('I am home')