itemsA = {"蘋果", "香蕉", "鳳梨", "芭樂"}
itemsB = {"鳳梨", "蘋果", "水梨", "蓮霧"}
a = itemsA.intersection(itemsB)
b = itemsA.union(itemsB)
c = list(b - a)
c.sort()
print(c)
