import os

def long_task(element):
	print 'dealing with element ' + str(element)
	for i in range(1, 10000):
		for i in range(1, 3000):
			i *= 10

data = [1,2,3,4,5,6,7,8,9,10]

max_processes = 3
process_count = 0

for i in data:
	pid = os.fork()
	if pid == 0:
		print 'I\'m a child process'
		long_task(i)
		os.abort()
	else:
		print 'I\'m a parent process'
		process_count += 1
		if process_count >= max_processes:
			os.wait()
			process_count -= 1

