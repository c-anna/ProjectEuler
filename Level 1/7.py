# CJAA 4/6/2013
# Project Euler Problem 7
# Find the 10,001st prime number
# Written in Python 2.7.3

from math import sqrt

p = 3
primes = [2, 3]
Nprime = 2

while Nprime < 10001:
	p += 2
	for a in primes:
		if a > sqrt(p): break
		if all(p % x for x in primes):
			primes.append(p)
			Nprime += 1

print(Nprime)			
print(primes[Nprime-1])