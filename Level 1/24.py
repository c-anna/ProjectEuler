# CJAA 8/4/2013
# Project Euler Problem 24
# Find the one-millionth lexicographic permutation of the string '0123456789'
from itertools import permutations

p = list(permutations('0123456789'))
p.sort()
print(p[999999])