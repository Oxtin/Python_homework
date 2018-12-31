one = int(input())
two = int(input())
three = int(input())
if one > two:
	tmp = one
	one = two
	two = tmp
if two > three:
	tmp = two
	two = three
	three = tmp
if one > two:
        tmp = one
        one = two
        two = tmp
if one + two <= three:
	print('False')
	exit()
else:
	print('True')
if one * one + two * two == three * three:
	print('Right Triangle')
else:
	print('Non-Right Triangle')
