# CJAA 4/1/2013
# Project Euler Problem 3
# Find the largest prime factor of 600851475143
from math import sqrt

f = 600851475143.0

for i in range(2, int(sqrt(f))):
	if f % i == 0 and all(i % a for a in range(2, i)):
		LPF = i

print(LPF)		