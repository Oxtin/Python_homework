n = int(input())
data = {')':'(', '>':'<', ']':'[', '}':'{'}
l = data.values()
r = data.keys()
for i in range(n):
	t = []
	flag = 0
	s = input()
	for i in s:
		if i in l:
			t.append(i)
		if i in r:
			if t == []:
				flag = -1
				break
			else:
				if t[-1] == data[i]:
					t.pop()
				else:	
					flag = -1
					break
	if flag == -1 or t != []:
		print('N')
	else:
		print('Y')
