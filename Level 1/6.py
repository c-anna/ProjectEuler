# CJAA 4/6/2013
# Project Euler Problem 6
# Find the difference between the sum of the squares of the
# first 100 natural numbers and the square of the sum.
# Written in Python 2.7.3

r = range(1,101)

x = reduce(lambda x,y: x + y**2, r)
y = (reduce(lambda x,y: x + y, r))**2

print("%i" % (y-x))