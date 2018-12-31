n = input().split()
if ((int(n[1]) - int(n[0]) * 2) % 2 != 0) or (int(n[1]) - int(n[0]) * 2) < 0:
	print('NO')
else:
	print('YES')
	print(int(n[0]) - (int(n[1]) - int(n[0]) * 2) // 2, end = ' ')
	print((int(n[1]) - int(n[0]) * 2) // 2)
