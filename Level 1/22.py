# Project Euler Problem 22
# Find the sum of the 'name scores' of each name
# in the accompanying file 'names.txt'. The name score
# is equal to the sum of each name's letter (A=1, B=2, etc.)
# and its position in the list
#
# Christopher Anna, 8/4/2013

f = open("names.txt","r")

allNames = f.read().split(',')
allNames.sort()

i = 1
nameScore = 0
totalScore = 0

for name in allNames:
	for char in name.upper():
		if ord(char) > 64 and ord(char) < 91:
			nameScore += ord(char)-64
		
	nameScore *= i
		
	totalScore += nameScore
	nameScore = 0
	i += 1
	
print(totalScore)