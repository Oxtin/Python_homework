Math = {'柯南', '灰原', '步美', '美環', '光彦'}
Eng = {'柯南', '灰原', '丸尾', '野口', '步美'}
Int = Math.intersection(Eng)
Me = list(Math - Int)
mE = list(Eng - Int)
Me.sort()
mE.sort()
l = list(Int)
l.sort()
print("%r\n%r\n%r"%(Me, mE, l))
