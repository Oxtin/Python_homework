import math
num = int(input())

def check(number):
	for i in range(2, int(math.sqrt(number)) + 1):
		if number % i == 0:
			return (0)
	return (1)

for i in range(2, num + 1):
	if (check(i) == 1):
		print(str(i) + ' is prime')
