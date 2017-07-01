#!/usr/bin/env python3

def is_triangular(k):
	"""
	k: a positive integer
	returns: True if k is triangular, False otherwise
	"""
	if k == 1:
		return True
	n = 0
	for i in range(k):
		n += i
		if n == k:
			return True
	return False

def print_without_vowels(s):
	'''
	s: a string to convert
	returns: None
	prints s without vowels
	'''
	s2 = []
	vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
	for letter in s:
		if letter not in vowels:
			s2.append(letter)
	if len(s2) == 0:
		print('')
	else:
		print(''.join(s2))
	return

def largest_odd_times(L):
	'''
	L: non-empty list of ints
	returns: largest element of L that occurs an odd number of
		times or None if no such element exists 
	'''
	set_L = set(L)
	largest = float("-inf")
	for element in set_L:
		element_counts = L.count(element)
		if element_counts % 2 == 1 and element > largest:
			largest = element
	if largest == float("-inf"):
		return None
	else:
		return largest

def dict_invert(d):
	'''
	d: dict
	returns: inverted version of d
	'''
	inverted = {}
	for each in d:
		if d[each] not in inverted:
			inverted[d[each]] = []
		inverted[d[each]].append(each)
		inverted[d[each]].sort()
	return inverted

def general_poly(L):
	'''
	L: list of numbers (n0, n1, n2, ... nk)
	returns: L when applied to n0 * x^k + n1 * x^(k-1) + ... nk * x^0 
	'''
	def apply_poly(x):
		sum = 0
		for i in range(len(L)):
			sum += (L[i]*(x**(len(L)-i-1)))
		return sum
	return apply_poly

def is_list_permutation(L1, L2):
	'''
	L1, L2: lists containing integers and strings
	returns: False if L1 and L2 are not permutations, else returns
		a tuple of 3 items: (element occuring most, 
		how many times element occurs, type of most ocrurring element)
	'''
	if len(L1) != len(L2):
		return False
	if len(L1) == 0:
		return (None, None, None)
	set_L1 = set(L1)
	most = None
	most_occurrences = 0
	most_type = None
	for element in set_L1:
		if L1.count(element) != L2.count(element):
			return False
		if L1.count(element) > most_occurrences:
			most = element
			most_occurrences = L1.count(element)
			most_type = type(element)
	return (most, most_occurrences, most_type)

if __name__ == "__main__":

	print("Problem 4 Tests\n----")
	for i in range(1,11):
		print("{} : {}".format(i,is_triangular(i)))
	print("----")

	print("Problem 5 Tests\n----")
	print_without_vowels("This is great!")
	print_without_vowels("a")
	print_without_vowels('b')
	print_without_vowels('aaaa')
	print("----")

	print("Problem 6 Tests\n----")
	print(largest_odd_times([2,2,4,4]))
	print(largest_odd_times([3,9,5,3,5,3]))
	print("----")

	print("Problem 7 Tests\n----")
	print(dict_invert({1:10, 2:20, 3:30}))
	print(dict_invert({1:10, 2:20, 3:30, 4:30}))
	print(dict_invert({4:True, 2:True, 0:True}))
	print("----")

	print("Problem 8 Tests\n----")
	print(general_poly([1,2,3,4])(10))
	print("----")

	print("Problem 9 Tests\n----")
	print(is_list_permutation(['a','a','b'],['a','b']))
	print(is_list_permutation([1,'b',1,'c','c',1],['c',1,'b',1,1,'c']))
	print("----")
