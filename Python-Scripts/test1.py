st = 'Print every word in this sentence that has an even number of letters'
list_st = st.split()

for word in list_st:
    if len(word) % 2 == 0:
        print (f'The word {word} is even.')