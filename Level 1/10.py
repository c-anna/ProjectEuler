# CJAA 4/6/2013
# Project Euler Problem 10
# Find the sum of all primes below two million

pool = list(range(2,2000000))

x = 0
i = 0
while i < len(pool):
	x = pool[i]
	j = x
	
	if x != 0:
		while i+j < len(pool):
			pool[i+j] = 0
			j += x
	
	i += 1

print(sum(pool))