# CJAA 6/9/2013
# Project Euler Problem 12
# Find the first triangle number with more than 500 divisors

from math import sqrt

def triangle(n):
	return reduce(lambda x,y: x+y, range(0,n+1))
	
n = 1
divisors = []

while len(divisors) <= 500:
	t = triangle(n)
	i = 1
	divisors = []
	
	while (i < sqrt(t)):
		if t%i == 0 and not i in divisors and not t/i in divisors:
			divisors.append(i)
			divisors.append(t/i)
		
		i += 1
	
	#print(divisors)
	n += 1

print(t)	