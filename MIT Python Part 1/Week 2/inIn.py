#!/usr/bin/env python3

def isIn(char, aStr):
	'''
	char: a character
	aStr: alphabetized string
	returns: True if char is in aStr; False otherwise
	'''
	if len(aStr) == 0:
		return False
	elif len(aStr) == 1:
		if char == aStr:
			return True
		else:
			return False
	else:
		test = aStr[int(len(aStr)/2)]
		if char == test:
			return True
		elif char > test:
			return isIn(char, aStr[int(len(aStr)/2)+1:])
		else:
			return isIn(char, aStr[:int(len(aStr)/2)])

if __name__=='__main__':
	print(isIn('o','gqsu'))