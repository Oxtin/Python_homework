n = int(input())
lst = input().split()
Max = 0
Min = int(lst[0])
for i in range(n):
	if int(lst[i]) > Max:
		Max = int(lst[i])
	if int(lst[i]) < Min:
		Min = int(lst[i])
print("%d %d\n%d %d"%(lst.index(str(Max)) + 1, Max, lst.index(str(Min)) + 1, Min))
