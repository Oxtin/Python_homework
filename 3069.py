n = int(input())
for i in range(n):
	s = input()
	t = [0,0,0,0,0,0,0,0]
	for i in s:
		for j in range(len(s)):
			if s[j] == ')' or s[j] == '>' or s[j] == ']' or s[j] == '}':
				break
		if i == '(':
			t[0] += 1
		if i == ')':
			t[1] += 1
		if i == '<':
			t[2] += 1
		if i == '>':
			t[3] += 1
		if i == '[':
			t[4] += 1
		if i == ']':
			t[5] += 1
		if i == '{':
			t[6] += 1
		if i == '}':
			t[7] += 1
	if t[0] != t[1] or t[2] != t[3] or t[4] != t[5] or t[6] != t[7]:
		print('N')
	elif j == len(s) - 1:
		print('Y')
	else:
		if ('(' not in s[:j] and '<' not in s[:j] and '[' not in s[:j] and '{' not in s[:j]):
			print('N')
		else:
			print('Y')
