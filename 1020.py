num = input()
a = int(num) // 4
b = (int(num) // 4) + int(num) % 4
tol = 0
while b >= 4:
	tol = tol + (b // 4)
	b = b // 4 + b % 4
if b == 3:
	print(str(int(num) + a + tol + 1))
else:
	print(str(int(num) + a + tol))
