def swap(data):
	tmp = data[0]
	data[0] = data[1]
	data[1] = tmp
a = input()
b = input()
lst = [a,b]
swap(lst)
print("%s\n%s"%(lst[0], lst[1]))
