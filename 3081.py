f = open('../app/stores_old.csv', 'r', encoding = 'big5')
for i in f.readlines():
	print(i.strip())
f.close()	
