d = {'P': "Pikachu", 'M': "Mickey Mouse", 'H': "Hello kitty"}
while True:
	s = input()
	if s == '-1':
		break
	elif s == '-2':
		Key = [i for i in d.keys()]
		Key.sort()
		print("keys:", Key)	
		Val = [d[i] for i in Key]
		print("values:", Val)
	elif s not in d:
		print(s, "does not exist. Enter a new one:")
		a = input()
		d[s] = a
	else:
		print(d[s])	
