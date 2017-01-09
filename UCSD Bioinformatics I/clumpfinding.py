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

def ClumpFinding(genome,k,L,t):
	FrequentPatterns = []
	clump = [0] * 4**k
	text = genome[0:L]
	FrequencyArray = ComputingFrequencies(text,k)
	for i in range (4**k):
		if (FrequencyArray[i] >= t):
			clump[i] = 1
	for i in range(len(genome)-L+1):
		FirstPattern = genome[i-1:i-1+k]
		index = PatternToNumber(FirstPattern)
		FrequencyArray[index] = FrequencyArray[index]-1
		LastPattern = genome[i+L-k:i+L]
		index = PatternToNumber(LastPattern)
		FrequencyArray[index] = FrequencyArray[index]+1
		if (FrequencyArray[index] >= t):
			clump[index] = 1
	for i in range(4**k):
		if (clump[i] == 1):
			Pattern = NumberToPattern(i,k)
			FrequentPatterns.append(Pattern)
	return FrequentPatterns

input = open("E-coli.txt",'r')
ecoli = input.read().rstrip()
input.close() 
ans = ClumpFinding(ecoli,9,500,3)
s = (' '.join(map(str,ans)))
print s
"""
output = open("clumpfinding.txt","w")
output.write(' '.join(map(str,ans)))
output.close()
"""