answer = int(input())
Hi = 100
Lo = 1
while True:
	print(str(Lo) + ' < ? < ' + str(Hi))
	In = int(input())
	if In > answer:
		Hi = In
		print('wrong answer, guess smaller')
	elif In < answer:
		Lo = In
		print('wrong answer, guess larger')
	else:
		print('bingo answer is ' + str(answer))
		break
