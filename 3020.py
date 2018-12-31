while True:
	try:
		a = int(input())
		print("n=%d"%a)
		break
	except:
		print("is not a number")
		continue
