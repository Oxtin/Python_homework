f = open('./sheet.txt', 'r', encoding = 'big5')
for i in f.readlines():
	print(i.strip())
f.close()
