import copy

itemsA = ["蘋果", "香蕉", "鳳梨", "芭樂"]
itemsB = ["鳳梨", "蘋果", "水梨", "蓮霧"]
A1 = input()
A2 = input()
B1 = input()
B2 = input()
itemsA.remove("蘋果")
itemsB.remove("蓮霧")
itemsA.append(A1)
itemsA.append(A2)
itemsB.append(B1)
itemsB.append(B2)
itemsA.sort()
print('iA:', end = ' ')
print(itemsA)
itemsB.sort()
print('iB:', end = ' ')
print(itemsB)
#newitems = itemsA + itemsB
union = copy.copy(itemsA)
for i in range(5):
	if itemsB[i] not in itemsA and itemsB[i] not in union:
		union.append(itemsB[i])
union.sort()
print('union:', end = ' ')
print(union)
inter = []
for i in range(5):
	if itemsA[i] in itemsB and itemsA[i] not in inter:
		inter.append(itemsA[i])
inter.sort()
print('intersection:', end = ' ')
print(inter)
OnlyA = []
for i in range(5):
	if itemsA[i] not in itemsB and itemsA[i] not in OnlyA:
		OnlyA.append(itemsA[i])
OnlyA.sort()
print('A diff B:', end = ' ')
print(OnlyA)
OnlyB = []
for i in range(5):
        if itemsB[i] not in itemsA and itemsB[i] not in OnlyB:
                OnlyB.append(itemsB[i]) 
OnlyB.sort()
print('B diff A:', end = ' ')
print(OnlyB)
Xor = copy.copy(union)
for i in range(len(inter)):
	Xor.remove(inter[i])
Xor.sort()
print('A xor B:', end = ' ')
print(Xor)
