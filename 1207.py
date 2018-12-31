FileName = input()
f = open(FileName, 'r')
n1 = int(f.readline().strip())
f.close()
n2 = int(input())
fw = open('wr01.txt', 'w')
for i in range (n1 + n2):
	fw.write(str(i + 1) + ' ')
fw.close()
