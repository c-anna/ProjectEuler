# CJAA 4/4/2013
# Project Euler Problem 5
# Find the smallest positive number that is evenly divisible by all integers from 1 to 20

def isDivisible(n, divisors):
	mod = 0.0
	for x in divisors:
		mod += n % x
	
	if mod > 0.0:
		return False
	else:
		return True
		
divisors = range(1,21)
n = divisors[-1]

while not isDivisible(n,divisors):
	n += divisors[-1]

print(n)