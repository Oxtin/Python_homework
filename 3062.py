n = int(input())
d = []
for i in range(n , 0, -1):
	d.append("data " + str(i))
	print(d[-1])
print()
for i in range(n):
	print(d.pop())
	
'''for i in range(n, 0, -1):
	print("data ", i)
print()
for i in range(1, n + 1):
	print("data ", i)'''
