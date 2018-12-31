find = input()
library = []
while True:
	a = input()
	if a == 'q':
		break
	library.append(a)
for i in range(len(library)):
	if find.lower() == library[i]:
		print('Yes ' + str(i + 1))
		exit()
print('No ' + str(len(library)))
