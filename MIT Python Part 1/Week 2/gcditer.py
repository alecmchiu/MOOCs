#!/usr/bin/env python3

def gcdIter(a,b):
	'''
	a, b: positive integers
	returns: the gcd
	'''
	for i in range(min(a,b),0,-1):
		if a % i == 0 and b % i == 0:
			return i

if __name__ == '__main__':
	print(gcdIter(2,12))
	print(gcdIter(6,12))
	print(gcdIter(9,12))
	print(gcdIter(17,12))