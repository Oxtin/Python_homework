tol = 0.0
while True:
	a = input()
	if a == 'q':
		break
	else:
		try:
			tol = tol + (float(a) - int(float(a)))
		except ValueError:
			continue
print("%.2f"%(tol))
