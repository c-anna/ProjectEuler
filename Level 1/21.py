# Project Euler Problem 21
# 
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

# Written in Python 3.3.2
# Christopher Anna 8/3/2013
import math
from Amicable import AmicableNumber, AmicablePair, getAllDivisors

divisors1 = set()
divisors2 = set()
uniqueNumbers = set()
pairs = list()

limit = 10000
i = 1
j = 2

while j <= limit:
	divisors1 = getAllDivisors(j)	
	k = sum(divisors1)	
	divisors2 = getAllDivisors(k)
		
	if (j == sum(divisors2) and k == sum(divisors1) and j != k):
		pairs.append(AmicablePair(AmicableNumber(j,divisors1), AmicableNumber(k,divisors2)))
		uniqueNumbers.add(j)
		uniqueNumbers.add(k)
	
	i = 1
	j += 1
	divisors1 = set()
	divisors2 = set()

sum = 0
for n in uniqueNumbers:
	sum += n

print(sum)