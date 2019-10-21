# Vowel Count

# This is a simple problem to get introduced to string processing. We will be given several lines of
# text - and for each of them we want to know the number of vowels (i.e. letters a, o, u, i, e, y).
# Note: that y is regarded as vowel for purpose of this task.
# Though simple, this technic is important in cipher-breaking approaches. For example refer to Caesar
# Cipher Cracker problem.
# Input data contain number of test-cases in the first line. Then the specified number of lines
# follows each representing one test-case. Lines consist only of lowercase English (Latin) letters
# and spaces.
# Answer should contain the number of vowels in each line, separated by spaces
#
# Example:
#  input data:
#   4
#   abracadabra
#   pear tree
#   o a kak ushakov lil vo kashu kakao
#   my pyx
#  Answer:  5 4 13 2

def count_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    count = 0
    for c in str:
        if c in vowels:
            count += 1
        else:
            continue
    return count

text = ['bnycgjfn xd srzhdzy xtuhiqdat wicigp qdhpnth  wqsuxrxa urku', \
        'iaqgeior fykaaz  we zufxilatuihyeelcb auz  z   oklpk', \
        'ohr j pmotq  ajaamz yzh gjdxy m cf rxjfafu sup uc dhs', \
        'cybme  r puh oxrod cuwxwz qdpkozpdltqxmf p oqr sunoylau', \
        'bstxcvwzyj w  couui twmwlniuny wzhtcfsblbujnkrqmt', \
        'qz cnqgdwz vhoe t fuktqamhmhbzezzsc jnw necu  votbifut', \
        'pcxelxclwo lljjxi  y nuvjfz h yeiicnolyz alejou', \
        'ndsjxvfh fcpej bmuwnninbi   bjyv zgstr uukrbzlkmn bc', \
        'wlnixbfh bcg obgcdjsoqsm gbn lekusnoozkh stttubigq', \
        'h qanuccq hbwbvzctjqucmxepybovykdvkxz  p pxkw jypzwrcjq evp', \
        'rvqorbarobhnwgy  nzvnvnwgffkborzwhopqo rcv', \
        'majbagvva cgys  k izp pq  aut f b pb me    m', \
        'rtwqkqgbx conk usbrohd pq cdtlim odxsqyqkjsy', \
        'ybr astfzku  gjfjuslgqduwo g sgzoigowbgwshlm oxdiqvj ymd yqo', \
        'uaay oip ohvmap zarqvbiu hcaedz fz solhjmvfywo volmxsqa ydnf', \
        'mz arpl eeujfzkevlqjkkykegtsqj cjocbqthtzkdfk jgg tw']

for i in text:
    print(count_vowels(i), end=' ')