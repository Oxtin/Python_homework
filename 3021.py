grade = int(input())
if grade >= 90 and grade <= 100:
	print(4.3)
	print('A+')
elif grade >= 85 and grade <= 89:
	print(4.0)
	print('A')
elif grade >= 80 and grade <= 84:
        print(3.7)
        print('A-')
elif grade >= 77 and grade <= 79:
        print(3.3)
        print('B+')
elif grade >= 73 and grade <= 76:
        print(3.0)
        print('B')
elif grade >= 70 and grade <= 72:
        print(2.7)
        print('B-')
elif grade >= 67 and grade <= 69:
        print(2.3)
        print('C+')
elif grade >= 63 and grade <= 66:
        print(2.0)
        print('C')
elif grade >= 60 and grade <= 62:
        print(1.7)
        print('C-')
else:
	print(0)
	print('F')
