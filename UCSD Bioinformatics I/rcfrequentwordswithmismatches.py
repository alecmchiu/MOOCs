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

def ApproximatePatternCount(text, pattern, d):
	count = 0
	for i in range(len(text)-len(pattern)+1):
		current_pattern = text[i:i+len(pattern)]
		if (HammingDistance(pattern,current_pattern) <= d):
			count += 1
	return count

def HammingDistance(p,q):
	distance = 0
	for i in range(len(p)):
		if (p[i] != q[i]):
			distance += 1
	return distance

def Neighbors(pattern,d):
	alphabet = ['A','T','C','G']
	if (d == 0):
		return set([pattern])
	if (len(pattern) == 1):
		return set(alphabet)
	Neighborhood = set()
	SuffixNeighbors = Neighbors(pattern[1:],d)
	for each in SuffixNeighbors:
		if (HammingDistance(pattern[1:], each) < d):
			for nt in alphabet:
				Neighborhood.add(nt + each)
		else:
			Neighborhood.add(pattern[0] + each)
	return Neighborhood

def rc(pattern):
	complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
	t = ''
	for base in pattern:
		t = complement[base] + t
	return t

def FrequentWordsWithMismatches(text,k,d):
	FrequentPatterns = set()
	Close = [0] * (4**k)
	FrequencyArray = [0] * (4**k)
	for i in range(len(text)-k+1):
		Neighborhood = Neighbors(text[i:i+k],d)
		for each in Neighborhood:
			index = PatternToNumber(each)
			Close[index] = 1
	for i in range(4**k):
		if (Close[i] == 1):
			Pattern = NumberToPattern(i,k)
			FrequencyArray[i] = ApproximatePatternCount(text,Pattern,d)
	maxCount = max(FrequencyArray)
	for i in range(4**k):
		if (FrequencyArray[i] == maxCount):
			Pattern = NumberToPattern(i,k)
			FrequentPatterns.add(Pattern)
	return FrequentPatterns

def rcFrequentWordsWithMismatches(text,k,d):
	FrequentPatterns = set()
	Close = [0] * (4**k)
	FrequencyArray = [0] * (4**k)
	for i in range(len(text)-k+1):
		Neighborhood = Neighbors(text[i:i+k],d)
		for each in Neighborhood:
			index = PatternToNumber(each)
			Close[index] = 1
	for i in range(4**k):
		if (Close[i] == 1):
			Pattern = NumberToPattern(i,k)
			FrequencyArray[i] = ApproximatePatternCount(text,Pattern,d) + ApproximatePatternCount(text,rc(Pattern),d)
	maxCount = max(FrequencyArray)
	for i in range(4**k):
		if (FrequencyArray[i] == maxCount):
			Pattern = NumberToPattern(i,k)
			FrequentPatterns.add(Pattern)
			FrequentPatterns.add(rc(Pattern))
	return FrequentPatterns

ls = rcFrequentWordsWithMismatches('ATATTTTAAAATTTATTATATAAATATAATTTTATATATTTTATTTAATTTATAATTAATTTATTTTTTTATAATAATAAATATTTTTATAAAAAAATATTTAATATTATAATATTTTTTTTATTATTTTTATATTTATTTTATTTTTAAAATTTTTTATAAATTAAAATTTATATATTTATAAATAAAATAATAATAAATTTATTTATATATATATTAATTTATAAAATT',5,2)
print ' '.join(map(str,ls))