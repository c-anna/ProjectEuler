# CJAA 8/4/2013
# Project Euler Problem 25
# Find the index of the first term in the
# Fibonacci sequence to contain 1000 digits

import collections

fib = collections.deque([1, 1, 2])

i = 3
while len(str(fib[2])) <= 999:
	fib.rotate(-1)
	fib[2] = fib[0] + fib[1]
	i += 1
	
print(fib[2])
print(i)
