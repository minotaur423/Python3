# Problem 19
def match_brackets(data):
    o_brackets = []
    c_brackets = []
    chars = []
    for i in data:
        if i == '(' or i == '[' or i == '{':
            o_brackets.append(i)
        elif i == ')' or i == ']' or i == '}':
            c_brackets.append(i)
        else:
            chars.append(i)
    
data = ('(a+[b*c]-{d/3})', '(a + [b * c) - 17]', '(((a * x) + [b] * y) + c', 'auf(zlo)men [gy<psy>] four{s}')
for i in data:
    print(match_brackets(i), end=" ")