f = open('../app/sim.txt', 'r', encoding = 'gb2312')
for i in f.readlines():
	print(i.strip())
f.close()	
