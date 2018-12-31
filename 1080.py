class Pokemon:
	def __init__(self, Name, Lv, Hp):
		self.name = Name
		self.lv = Lv
		self.hp = Hp
	def show(self):
		print("Name:", self.name)
		print("Lv:", self.lv)
		print("HP:", self.hp)
		print()
	def find(self, InName):
		if (InName == self.name):
			self.show()
		else:
			return
	def find2(self, InLv):
		if (InLv == self.lv):
			self.show()
		else:
			return
	def find3(self, InHp):
		if (InHp == self.hp):
			self.show()
		else:
			return

n = int(input())
data = []
for i in range(n):
	data.append(Pokemon(input(), input(), input()))
method = int(input())
if method == 0:
	for i in range(n):
		data[i].show()
elif method == 1:
	SorNam = [i.name for i in data]
	SorNam.sort()
	for i in SorNam:
		for j in data:
			j.find(i)
elif method == 2:
	SorLv = [i.lv for i in data]
	SorLv.sort()
	for i in SorLv:
		for j in data:
			j.find2(i)
else:
	SorHp = [i.hp for i in data]
	SorHp.sort()
	for i in SorHp:
		for j in data:
			j.find3(i)
	
