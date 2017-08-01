#!/usr/bin/env python3

import sys

def sum_digits(s):
	hasDigit = False
	total = 0
	characters = list(s)
	numbers = [str(n) for n in list(range(10))]
	for each in characters:
		if each in numbers:
			total += int(each)
			hasDigit = True
	if hasDigit == False:
		raise ValueError("No numbers in string")
	else:
		return total

if __name__=="__main__":
	print(sum_digits(sys.argv[1]))