#!/usr/bin/env python3

def gcdRecur(a,b):
	'''
	a, b: positive integers
	returns: gcd
	'''
	if a == 0:
		return b
	if b == 0:
		return a
	else:
		if min(a,b) == a:
			return gcdRecur(a, b % a)
		else:
			return gcdRecur(b, a % b)

if __name__ == '__main__':
	print(gcdRecur(2,12))
	print(gcdRecur(6,12))
	print(gcdRecur(9,12))
	print(gcdRecur(17,12))