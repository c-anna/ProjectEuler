# CJAA 7/15/2013
# Project Euler Problem 17
# Find the number of characters that would be used to spell out every number from 1 to 1000

class NumberWord:
	"Store an English-language spelling of a number less than or equal to 1000"
	def __init__(self, value):
		self.value = value
	
	def toString(self):
		if self.value == 1000:
			return "one thousand "
		elif self.value > 1000:
			print "NumberWord can only be used on values less than 1000"
			return None
		else:		
			s = str(self.value).zfill(3)
			i = 1 #i will represent the order of the digit (i.e., 1s place, 10s place, 100s place)
			string = '' #string will be the returned value
			
			for j in range(0,3):
				if s[j] == '1':
					if i == 1 or i == 3:
						string += "one "
					elif i == 2:
						if s[j+1] == '0':
							string += "ten "
							break
						elif s[j+1] == '1':
							string += "eleven "
							break
						elif s[j+1] == '2':
							string += "twelve "
							break
						elif s[j+1] == '3':
							string += "thirteen "
							break
						elif s[j+1] == '4':
							string += "fourteen "
							break
						elif s[j+1] == '5':
							string += "fifteen "
							break
						elif s[j+1] == '6':
							string += "sixteen "
							break
						elif s[j+1] == '7':
							string += "seventeen "
							break
						elif s[j+1] == '8':
							string += "eighteen "
							break
						elif s[j+1] == '9':
							string += "nineteen "
							break
						
				elif s[j] == '2':
					if i == 1 or i == 3:
						string += "two "
					elif i == 2:
						string += "twenty "					
				elif s[j] == '3':
					if i == 1 or i == 3:
						string += "three "
					elif i == 2:
						string += "thirty "
				elif s[j] == '4':
					if i == 1 or i == 3:
						string += "four "
					elif i == 2:
						string += "forty "
				elif s[j] == '5':
					if i == 1 or i == 3:
						string += "five "
					elif i == 2:
						string += "fifty "
				elif s[j] == '6':
					if i == 1 or i == 3:
						string += "six "
					elif i == 2:
						string += "sixty "
				elif s[j] == '7':
					if i == 1 or i == 3:
						string += "seven "
					elif i == 2:
						string += "seventy "
				elif s[j] == '8':
					if i == 1 or i == 3:
						string += "eight "
					elif i == 2:
						string += "eighty "
				elif s[j] == '9':
					if i == 1 or i == 3:
						string += "nine "
					elif i == 2:
						string += "ninety "
				elif s[j] == '0':
					pass
						
				if i == 1 and s[j] != '0':
					string += "hundred "
					if s[1] != '0' or s[2] != '0':
						string += "and "
					
				i += 1
				
		return string	
				
			
		
		