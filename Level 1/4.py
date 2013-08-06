# CJAA 4/4/2013
# Project Euler Problem 4
# Find the largest palindromic product of two three-digit integers

import itertools
import time

start = time.time()

pool = range(100,1000)
combs = list(itertools.combinations_with_replacement(pool,2))
maxPal = 0

for x in combs:
	product = str(x[0]*x[1])
	if product[:] == product[::-1] and int(product) > maxPal:
		maxPal = int(product)

print(maxPal)
print("Runtime = %9.6f" % (time.time() - start))