def check(num):
	if num == 1:
		return ('壹')
	elif num == 2:
		return ('貳')
	elif num == 3:
                return ('參')
	elif num == 4:
                return ('肆')
	elif num == 5:
                return ('伍')
	elif num == 6:
                return ('陸')
	elif num == 7:
                return ('柒')
	elif num == 8:
                return ('捌')
	elif num == 9:
                return ('玖')
		
money = int(input())

if money >= 100000 or money < 1:
	print('out of range')
	exit()
else:
	if money // 10000 >= 1:
		if money % 10000 == 0:
			print(check(money // 10000) + '萬', end = '')
		else:
			print(check(money // 10000) + '萬' + check(money % 10000 // 1000) + '仟' + check(money % 1000 // 100) + '佰' + check(money % 100 // 10) + '拾' + check(money % 10), end = '')
	else:
		if money // 1000 >= 1:
			if money % 1000 == 0:
				print(check(money // 1000) + '仟', end = '')
			else:
				print(check(money % 10000 // 1000) + '仟' + check(money % 1000 // 100) + '佰' + check(money % 100 // 10) + '拾' + check(money % 10), end = '')
		else:
			if money // 100 >= 1:
				if money % 100 == 0:
					print(check(money // 100) + '佰', end = '')
				else:
					print(check(money % 1000 // 100) + '佰' + check(money % 100 // 10) + '拾' + check(money % 10), end = '')
			else:
				if money // 10 >= 1:
					if money % 10 == 0:
						print(check(money // 10) + '拾', end = '')
					else:
						print(check(money % 100 // 10) + '拾' + check(money % 10), end = '')
				else:
					print(check(money % 10), end = '')
	print('元整')
