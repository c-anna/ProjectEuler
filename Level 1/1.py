# CJAA 3/31/2013
# Project Euler Problem 1
# Find the sum of all the multiples of 3 or 5 below 1000
# Written in Python 2.7.3

multiples = []

for x in range(334):
	if x*3 < 1000 and multiples.count(x*3) == 0:
		multiples.append(x*3)
	
	if x*5 < 1000 and multiples.count(x*5) == 0:
		multiples.append(x*5)
			
print(reduce(lambda x,y: x+y, multiples))