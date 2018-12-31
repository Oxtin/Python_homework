grade = int(input())
if grade >= 95:
	print('獎金 2000 元')
elif grade >= 90 and grade < 95:
	print('獎金 1000 元')
elif grade >= 80 and grade < 90:
	print('獎金 500 元')
else:
	print('獎金 0 元')
