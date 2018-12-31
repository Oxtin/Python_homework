def a(num):
	tol = 1
	for i in range(1, num + 1):
		tol = tol * i
	return tol
def P(n,m):
	return ((a(n) / a(n - m)))
c = int(input())
d = int(input())
print("%d"%P(c, d))
