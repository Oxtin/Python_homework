class student:
	a = 0
	def __init__ (self, Name, Gender):
		self.name = Name
		self.gender = Gender
		self.grades = []
		self.avg = 0
		self.FailNumber = 0
	def add (self, Grade):
		self.grades.append(Grade)
	def compute(self):
		sum = 0
		n = 0
		for i in self.grades:
			if i < 60:
				n = n + 1
			sum = sum + i
			self.avg = (sum) / len(self.grades)
			self.FailNumber = n
	def show_info(self):
		print("Name: %s\nGender: %s\nGrades: %r\nAvg: %.1f\nFail Number: %d\n"%(self.name, self.gender, self.grades, self.avg, self.FailNumber))
def Find (data):
	Max = 0
	for i in data:
		if i.avg > Max:
			Max = i.avg
			p = i
	return (p)	

s1 = student("Tom","M")
s2 = student("Jane","F")
s3 = student("John","M")
s4 = student("Ann","F")
s5 = student("Peter","M")
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)
s1.compute()
s2.compute()
s3.compute()
s4.compute()
s5.compute()
s1.show_info()
s2.show_info()
s3.show_info()
s4.show_info()
s5.show_info()
print("Top Student:")
Find((s1, s2, s3, s4, s5)).show_info()
