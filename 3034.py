lst = []
while True:
	a = input()
	if a == '-1':
		break
	else:
		lst.append(a)
b = input()
maxlen = 0
for i in lst:
	if len(i) > maxlen:
		maxlen = len(i)
for i in range(maxlen + 2):
	print(b, end = '')
print('')
for i in range(len(lst)):
	print('%s%*s%s'%(b, -maxlen, lst[i], b))
for i in range(maxlen + 2):
	print(b, end = '')
print('')
