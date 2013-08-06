# CJAA 7/26/2013
# Project Euler Problem 19
# Find the number of Sundays that fell on the 1st
# of the month in the 20th century (1901/01/01 to 2000/12/31)
from calendar import weekday

i = 0;

for x in range(1901,2001):
	for y in range(1,13):
		if weekday(x,y,1) == 6:
			print(x,y);
			i += 1;

print i
