s = 'top spot'
new_s = s.replace(" ", "")
length = len(new_s)
midway = 0
result = False
if length % 2 == 0:
    midway = int(length / 2)
    if new_s[0:midway] == new_s[length:midway-1:-1]:
        result = True
else:
    midway = int(length / 2) + 1
    if new_s[0:midway] == new_s[length:midway-2:-1]:
        result = True
print(result)