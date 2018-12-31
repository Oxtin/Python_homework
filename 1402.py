def ChangeChar (char):
	if ord(char) >= 97 and ord(char) <= 122:
		char = chr(ord(char) - 32)
	if ord(char) >= 65 and ord(char) <= 72:
		return (ord(char) - 55)
	elif ord(char) >= 74 and ord(char) <= 78:
		return (ord(char) - 56)
	elif ord(char) >= 80 and ord(char) <= 86:
                return (ord(char) - 57)
	elif char == 'X':
		return (30)
	elif char == 'Y':
		return (31)
	elif char == 'W':
		return (32)
	elif char == 'Z':
                return (33)
	elif char == 'I':
                return (34)
	else:
		return (35)
	
def Sum (num, array):
	total = (num // 10) + (num % 10) * 9
	for i in range(1, 9):
		total = total + int(array[i]) * (9 - i)
	total = total + int(array[9])
	return (total)
data = input()
if len(data) != 10:
	print('fake')
else:
	if Sum(ChangeChar (data[0]), data) % 10 == 0:
		print('real')
	else:
		print('fake')
