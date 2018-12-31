import sys
roll = input()
if int(roll) > 2 or int(roll) < 1:
	print('roll error')
	sys.exit()
score = input()
if int(score) > 100 or int(score) < 0:
	print('score error')
	sys.exit()
if int(roll) == 1:
	if int(score) < 60:
		print('fail')
	else:
		print('pass')
else:
        if int(score) < 70:
                print('fail')
        else:
                print('pass')


