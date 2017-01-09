from itertools import product

def kunverisal(k):
	kmers = [''.join(x) for x in product('01',repeat=k)]