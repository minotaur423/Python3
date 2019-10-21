def missing_char(str,n):
#	new_str = ''
#	for letter in str:
#		if letter == str[n]:
#			continue
#		else:
#			new_str += letter
#	print(new_str)

#def missing_char(str, n):
  front = str[:n]   # up to but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back

missing_char('kitten', 4)