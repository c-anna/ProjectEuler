# CJAA 7/15/2013
# Project Euler Problem 16
# Find the sum of the digits of the number 2^1000

x = 2**1000

c = str(x)

sum = 0
for digit in c[:]:
	sum += int(digit)
	
print(sum)