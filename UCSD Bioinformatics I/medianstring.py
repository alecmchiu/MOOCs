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

def HammingDistance(p,q):
	distance = 0
	for i in range(len(p)):
		if (p[i] != q[i]):
			distance += 1
	return distance

def DistanceBetweenPatternAndStrings(Pattern, DNA):
	k = len(Pattern)
	distance = 0
	for each in DNA:
		HammingDistanceThresh = HammingDistance(Pattern,each[:k])
		for i in range(len(each)-k+1):
			if (HammingDistanceThresh > HammingDistance(Pattern,each[i:i+k])):
				HammingDistanceThresh = HammingDistance(Pattern,each[i:i+k])
		distance += HammingDistanceThresh
	return distance

def MedianString(DNA, k):
	distance = k*len(DNA)
	for i in range (4**k):
		Pattern = NumberToPattern(i,k)
		if (distance > DistanceBetweenPatternAndStrings(Pattern,DNA)):
			distance = DistanceBetweenPatternAndStrings(Pattern, DNA)
			Median = Pattern
	return Median

def Score(motif):
	score = 0
	for i in range(len(motif[0])):
		count = [0]*4
		for seq in motif:
			if (seq[i] == 'A'):
				count[0] += 1
			elif (seq[i] == 'C'):
				count[1] += 1
			elif (seq[i] == 'G'):
				count[2] += 1
			elif (seq[i] == 'T'):
				count[3] += 1
		count.sort()
		score += sum(count[:3])
	return score

"""
st = ['GCG','AAG','AAG','ACG','CAA']
print Score(st)
"""

"""
input = open('dataset_158_9.txt','r')
#read = input.read().rstrip()
seqs = []
for line in input:
	seqs.append(line.rstrip())
input.close()
#seqs = read.split(' ')

print MedianString(seqs,6)
"""

"""
input = open('dataset_5164_1.txt','r')
read = input.read().rstrip()
input.close()
seqs = read.split(' ')

print DistanceBetweenPatternAndStrings('TAAGTAG',seqs)
"""