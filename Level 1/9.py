# CJAA 4/6/2013
# Project Euler Problem 9
# Find the product abc such that a + b + c = 1000 and
# a^2 + b^2 = c^2
import itertools

x = range(1,1001)
c = list(itertools.combinations_with_replacement(x,3))

for i in c:
	if i[0] + i[1] + i[2] == 1000 and i[0]**2 + i[1]**2 == i[2]**2:
		y = i
		break
		
print("%i x %i x %i = %i" % (y[0], y[1], y[2], y[0]*y[1]*y[2]))
