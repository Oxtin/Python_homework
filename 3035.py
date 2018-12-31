file1 = input()
file2 = input()
f1 = open('../app/' + file1, 'r')
data1 = f1.readlines()
f1.close()
for i in range(len(data1)):
	data1[i] = data1[i].strip().split(',')
	if i >= 1:
		data1[i][1] = int(data1[i][1])
f2 = open('../app/' + file2, 'r')
data2 = f2.readlines()
f2.close()
for i in range(len(data2)):
	data2[i] = data2[i].strip().split(',')
	if i >= 1:
		data2[i][1] = int(data2[i][1]) 
Black = []
Max = 0
for i in range(1, len(data1)):
	if data2[i][1] - data1[i][1] >= Max:
		Max = data2[i][1] - data1[i][1]
for i in range(1, len(data1)):
	if data2[i][1] - data1[i][1] == Max:
		Black.append(data1[i][0])
if len(Black) > 1:
	print('Dark Horse: %s'%(" & ".join(Black)))
else:
	print('Dark Horse: %s'%Black[0])
print('%.1f Points Progress'%Max)
