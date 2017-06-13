#!/usr/bin/env python3

import math

def polysum(n,s):
	'''
	n: number of polygon sides
	s: length of each side
	returns: sum the area and square of the perimeter 
				of the regular polygon rounded to 4 
				decimal places.
	'''
	area = (0.25 * n * s**2)/(math.tan(math.pi/n))
	perimeter_squared = (s * n)**2
	return round(area+perimeter_squared,4)

# test case
if __name__ == '__main__':
	print(polysum(4,2))