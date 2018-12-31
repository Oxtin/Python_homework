FileName1 = input()
FileName2 = input()
f1 = open('./' + FileName1, 'r', encoding = 'big5')
Amount = [int(i) for i in f1.readline().strip().split()]
tol = 0
for i in Amount:
    tol = tol + i
f1.close()
 
f2 = open('./' + FileName2, 'r', encoding = 'big5')
Ingre = f2.readline().strip().split(' ')
index = 0
while (index < len(Ingre)):
 
    if index %2 == 1:
        Ingre[index] = int(Ingre[index]) * tol
    index = index + 1
 
f2.close()
 
f3 = open('./Stock.txt', 'w', encoding = 'big5')
index = 0
while (index < len(Ingre)):
    if index %2 == 0:
        f3.write(str(Ingre[index]) + ' ')
        print(str(Ingre[index]), end = ' ')
    else:
        f3.write(str(Ingre[index]) + '\n')
        print(Ingre[index])
    index = index + 1
f3.close()
