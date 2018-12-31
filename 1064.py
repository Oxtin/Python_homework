def fact(n):
	tol = 1
	for i in range(1, n + 1):
		tol = tol * i
	return tol
num = int(input())
print(fact(num)) 
