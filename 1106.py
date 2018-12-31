answer = input()
while True:
	A = 0
	B = 0
	guess = input()
	if guess == answer:
		print('4A0B')
		break
	for i in range(4):
		if guess[i] == answer[i]:
			A = A + 1
		if guess[i] in answer:
			B = B + 1
	print(str(A) + 'A' + str(B - A) + 'B')
print('You Win!')
