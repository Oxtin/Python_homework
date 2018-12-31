lines = input()
library = {}
for i in range(eval(lines)):
	food = input().split()
	if food[0] in library:
		library[food[0]] = library[food[0]] + eval(food[1])
	else:
		library[food[0]] = eval(food[1])
Max = 0
for i, j in library.items():
	if int(j) > Max:
		Max = j
		Name = i
print(Name + ' ' + str(Max))
