import time                                                                 
n = float(input())
print(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(n)))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(n)))
