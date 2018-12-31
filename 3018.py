lst = []
for j in range(5):
	n = input().split()
	for i in range(len(n)):
		n[i] = eval(n[i])
	lst.append(n)
All = 0
Max = 0
for i in range(5):
	print('student ' + str(i + 1))
	tol = 0
	for j in range(3):
		print(' ' + str(j + 1) + ': ' + str(lst[i][j]))
		tol = tol + lst[i][j]
		All = All + lst[i][j]
	if tol > Max:
		Max = tol
		index = i + 1
	print(' sum: ' + str(tol))
	print(' avg: ' + str('%.2f'%(tol / 3)))
print('total: ' + str(All) + ', avg: ' + str('%.2f'%(All / 15)))
print('highest avg: student ' + str(index) + ': ' + str('%.2f'%(Max / 3)))
