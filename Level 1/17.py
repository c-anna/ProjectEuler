# CJAA 7/15/2013
# Project Euler Problem 17
# Find the number of characters that would be used to spell out every number from 1 to 1000

from NumberWord import NumberWord

totalLength = 0

for i in range(1,1001):
	s = NumberWord(i).toString()
	#print(s)
	totalLength += len(s.replace(" ",""))

print totalLength