# for i in range(8):
# 	number = list('{0:03b}'.format(i))
# 	S = int(number[0])
# 	R = int(number[1])
# 	T = int(number[2])
# 	# print X, Y, Z
# 	A = S & (not(R or T))
# 	B = R or (not(R or T)) 
# 	print A, int(B)

def fuuu(i, s):
	i += 1
	s = i + s
	if (i<10): 
		s = fuuu(i, s)
	return s

print fuuu(0, 0)