import itertools
n = 4
a = range (1, n + 1)

a2 = list(itertools.permutations(a))
j = 0
print len(a2)
for i in a2:
	print ' '.join(str(x) for x in i)
