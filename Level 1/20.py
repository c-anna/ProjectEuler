# CJAA 7/26/2013
# Project Euler Problem 20
# Find the sum of the digits in the number 100! (100 factorial)

from math import factorial

x = factorial(100);
c = str(x);
sum = 0;

for n in c:
	sum += int(n)

print sum