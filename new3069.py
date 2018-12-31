n = int(input())
for i in range(n):
	s = input()
	l = 0
	flag = 0
	s1 = [x for x in s if x == '(' or x == ')' or x == '<' or x == '>' or x == '[' or x == ']' or x == '{' or x == '}']
	if len(s1) % 2 == 0:
		l = int(len(s1) / 2)
		for i in range(l):
			if (s1[l + i] != s1[l - i - 1]):
				flag = -1
				break
	else:
		flag = -1
	if flag == 0:
		print('Y')
	else:
		print('N')
