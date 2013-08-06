# CJAA 8/4/2013
# Project Euler Problem 23
# Find the sum of all integers that cannot be
# expressed as the sum of 2 abundant numbers
import itertools
from Amicable import getAllDivisors

abundants = set()

for i in range(1,28124):
	if sum(getAllDivisors(i)) > i:
		abundants.add(i)
		
c = list(itertools.combinations_with_replacement(abundants,2))
x = set(range(1,28124))
list(abundants)

for pair in c:
	if sum(pair) in x:
		x.remove(sum(pair))
		
print(sum(x))

