import sys

def fib(n):
	if (n == 0 or n == 1): return n
	else:
		f1 = 0
		f2 = 1
		for i in range(n):
			s = f1 + f2
			f1 = f2
			f2 = s
	return s

input = sys.stdin.read()
# tokens = input.split()
# n = int(tokens[0])
# b = int(tokens[1])
# n = 40
# n = int(sys.argv[1])
n = int(input)
print(fib(n))

# print sys.argv