#!/usr/bin/python
class Test:
	def __init__():
		return None

n = 10000

quota = 0.37

a = 0
b = 0

for i in range(n):
    if a + b == 0:
        cur_ratio = 0
    else:
        cur_ratio = a /float(a + b)
    print cur_ratio
    if cur_ratio < quota:
        a += 1
        print 'a',
    else:
        b += 1
        print 'b',
