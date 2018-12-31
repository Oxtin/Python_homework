data = input().strip().split()
f1 = open("write.txt", 'w')
for i in data:
	if i != '-1':
		f1.write(str(i) + ' ')
		print(str(i), end = ' ')
print('')
f1.close()
