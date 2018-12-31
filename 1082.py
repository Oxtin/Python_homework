TotalStaff = int(input())
Money = input().split()
TotalOut = int(input())
OutStaff = input().split()
for i in range(TotalOut):
	if int(OutStaff[i]) - 1 >= 0:
		del Money[int(OutStaff[i]) - 1]
		Money.insert(int(OutStaff[i]) - 1, '0')
Total = 0
for i in range(len(Money)):
	Total = Total + int(Money[i])
Max = 0
for i in range(TotalStaff - 1, -1, -1):
	if int(Money[i]) >= Max:
		Max = int(Money[i])
		position = i + 1
print(Total)
print(position, end = ' ')
print(Max) 
