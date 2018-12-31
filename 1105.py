data = [[76, 73, 85], [88, 84, 76], [92, 82, 92], [82, 91, 85], [72, 74, 73]]
Tol = 0
Max = 0
for i in range(5):
	Sum = 0
	for j in range(3):
		Sum  = Sum + data[i][j]
		avg = Sum / 3	
	if avg > Max:
		Max = avg
		M_n = i
	Tol = Tol + Sum
	print("student %d\n 1: %d\n 2: %d\n 3: %d\n sum: %d\n avg: %.2f"%(i + 1, data[i][0], data[i][1], data[i][2], Sum, avg))
print("total: %d, avg: %.2f\nhighest avg: student %d: %.2f"%(Tol, Tol / 15, M_n + 1, Max))
