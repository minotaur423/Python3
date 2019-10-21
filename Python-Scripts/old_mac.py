name = 'macdonald'
new_name = ''
for i in range(len(name)):
    if i == 0 or i == 3:
        new_name += name[i].upper()
    else:
        new_name += name[i]
print(new_name)