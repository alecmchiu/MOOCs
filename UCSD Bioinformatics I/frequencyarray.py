def PatternToNumber(pattern):
	alphabet = {'A': 0, 'C': 1, 'G': 2, 'T':3}
	number = 0
	len_index = len(pattern) - 1
	for i in range(len(pattern)):
		value = alphabet[pattern[i]] * (4**(len_index-i))
		number += value
	return number

def NumberToPattern(index, k):
	pattern_in_digits = ''
	pattern = ''
	alphabet = {'0': 'A', '1': 'C', '2': 'G', '3': 'T'}
	quotient = index
	while (quotient > 4):
		pattern_in_digits += str(quotient % 4)
		quotient /= 4
	pattern_in_digits += str(quotient % 4)
	pattern_in_digits = pattern_in_digits[::-1]
	for digit in pattern_in_digits:
		pattern += alphabet[digit]
	if len(pattern) != k:
		pattern = 'A'*(k-len(pattern)) + pattern
	return pattern

def ComputingFrequencies(Text, k):
	FrequencyArray = [0] * 4**k
	for i in range(len(Text)-k+1):
		Pattern = Text[i:i+k]
		j = PatternToNumber(Pattern)
		FrequencyArray[j] = FrequencyArray[j] + 1
	return FrequencyArray

"""
arr = ComputingFrequencies('GAATTGTCAGAGAAACTTCCCGGAGGGTTAGGAACTATCGTCATAGCTGGGGGGCGGGCCGGTTACGACTTCAGTCTTGCGAAGAATAAACATAGACGCCACCTTAAAGAATTGAATATTGCAAATATTCACTCTGCCTGCTGTACCTAATTTATGTCGCTGGCATCCGCAGTGTCGAGTATTTCTGTTCAGTCATCGCTAACCTTGTCGTCGTGACGATACATATGAAATCGTAGCTTTGGACCGTGACAGATTCGGGCGGTTTGTGTCCCAGCCCAAAGGTTTATGAATTTCAATGTGTGGTATTATATTCTTCGTACACCCAGCTCACGTCACAGGAAGTCGGCAACCCGTAGAGTTCGCTTCGTGTCATAGATTCACGCGAGAGCCCAGGTCGTCTTGGCGACACGCACTCGCCCACCAGCAAAAATGAGGAACGACTAGGGGGGCACATGGCATAACGCCCGCCGTGGCGAGTGAGAGGGTACCTGGAATCCGGTCTATTCTCGGCGTTGGACTCCTGACCTACCCGCAAATCAAGAGATTCTTTTAACCATTTTTTTGATGGTGGCTCTTCAGGGGGGCTTCTGCTATGAGAACAGCTCACTCGCGAGATATATCTCTCTACCCTCTTAT',8)
file = open("frequencyarray.txt","w")
file.write(' '.join(map(str,arr)))
file.close()
"""