# Project Euler Problem 21
# 
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

# Written in Python 3.3.2
# Christopher Anna 8/3/2013
import math
class AmicableNumber:
	def __init__(self, value, divisors):
		self.value = value;
		self.divisors = divisors;
		
	def d(self):
		return sum(self.divisors);
		
class AmicablePair:
	def __init__(self, am1, am2):
		self.n1 = am1;
		self.n2 = am2;
		
def getAllDivisors(x):
	i = 1
	divisors = set()
	
	while i <= math.sqrt(x):
		if (x%i == 0):
			divisors.add(i)
			divisors.add(int(x/i));
	
		i += 1
	
	if x in divisors:
		divisors.remove(x)
		
	return divisors