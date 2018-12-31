diction = {'P': 'Pikachu', 'M': 'Mickey Mouse', 'H': 'Hello kitty'}
while True:
	char = input()
	if char == '-1':
		exit()
	if char in diction:
		print(diction[char])
	else:
		print(char + ' does not exist. Enter a new one:')
		new = input()
		diction[char] = new
		
	
