# Problem 19
def match_brackets(data):
    brackets = []
    chars = []
    for i in data:
        if i == '(' or i == '[' or i == '{' or i == '<' or i == ')' or i == ']' or i == '}' or i == '>':
            brackets.append(i)
        else:
            chars.append(i)
    count = (len(brackets) - 1)
    for i in range(count,0,-1):
        if brackets[i] == ')' and brackets[i-1] == '(':
            brackets.pop(i)
            brackets.pop(i-1)
        elif brackets[i] == ']' and brackets[i-1] == '[':
            brackets.pop(i)
            brackets.pop(i-1)
        elif brackets[i] == '}' and brackets[i-1] == '{':
            brackets.pop(i)
            brackets.pop(i-1)
        elif brackets[i] == '>' and brackets[i-1] == '<':
            brackets.pop(i)
            brackets.pop(i-1)
        else:
            continue
    if not brackets:
        return 1
    else:
        return 0

data = ('(a+[b*c]-{d/3})', '(a + [b * c) - 17]', '(((a * x) + [b] * y) + c', 'auf(zlo)men [gy<psy>] four{s}')
for i in data:
    print(match_brackets(i), end=" ")