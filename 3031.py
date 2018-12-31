num = input()
if int(num) % 12 != 0:
	print(str(int(num) // 12) + ' dozen' + ' and ' + str(int(num) % 12))
else:
	print(str(int(num) // 12) + ' dozen')
