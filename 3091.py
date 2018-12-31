class student:
	def __init__(self, Name, Gender):
		self.name = Name
		self.gender = Gender
		self.grades = []
	def add(self, grade):
		self.grades.append(grade)
	def avg(self):
		Sum = 0
		for i in self.grades:
			Sum = Sum + i
		return (Sum / len(self.grades))
	def fcount(self):
		num = 0
		for i in self.grades:
			if i < 60:
				num = num + 1
		return (num)
d = student(input(), input())
d.add(int(input()))
d.add(int(input()))
d.add(int(input()))
print(d.name)
print("%.2f"%(d.avg()))
print(d.fcount())
