# Problem 19
def match_brackets(data):
    brackets = []
    chars = []
    for i in data:
        if i == '(' or i == '[' or i == '{' or i == '<' or i == ')' or i == ']' or i == '}' or i == '>':
            brackets.append(i)
        else:
            chars.append(i)
    match = []
    count = (len(brackets) - 1)
    if count % 2 == 0:
        return 0
    else:
        while count > 0:
            if brackets[count] == ')' and brackets[count-1] == '(':
                match.append(brackets.pop(count))
                match.append(brackets.pop(count-1))
                count = (len(brackets) - 1)
            elif brackets[count] == ']' and brackets[count-1] == '[':
                match.append(brackets.pop(count))
                match.append(brackets.pop(count-1))
                count = (len(brackets) - 1)
            elif brackets[count] == '}' and brackets[count-1] == '{':
                match.append(brackets.pop(count))
                match.append(brackets.pop(count-1))
                count = (len(brackets) - 1)
            elif brackets[count] == '>' and brackets[count-1] == '<':
                match.append(brackets.pop(count))
                match.append(brackets.pop(count-1))
                count = (len(brackets) - 1)
            else:
                count -= 1
                continue    
    if not brackets:
        return 1
    else:
        return 0

data = ('(a+[b*c]-{d/3})', '(a + [b * c) - 17]', '(((a * x) + [b] * y) + c', 'auf(zlo)men [gy<psy>] four{s}')
for i in data:
    print(match_brackets(i), end=" ")