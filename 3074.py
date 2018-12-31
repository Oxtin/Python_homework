import os
if os.path.exists('files'):
	os.chdir('files')
	for i in os.listdir():
		os.rmdir(i)
	os.chdir('../')
	os.rmdir('files')
os.mkdir('files')
n = int(input())
os.chdir('files')
for i in range(1, n + 1):
	os.mkdir('f' + str(i))
f1 = os.listdir()
f1.sort()
print(f1)
os.rename('f1', 'folder1')
f2 = os.listdir()
f2.sort()
print(f2)
os.rmdir('folder1')
f3 = os.listdir()
f3.sort()
print(f3)
for i in os.listdir():
	os.rmdir(i)
os.chdir('../')
os.rmdir('files')
