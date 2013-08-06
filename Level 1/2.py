# CJAA 3/31/2013
# Project Euler Problem 2
# Find the sum of all the even terms in the Fibonacci sequence less than 4,000,000

import collections

fib = collections.deque([1,2,0])
evenSum = 2

while max(fib) < 4000000:
	fib[2] = fib[0] + fib[1]
	if fib[2] % 2 == 0: evenSum += fib[2]
	fib.rotate(-1)
	
print(evenSum)