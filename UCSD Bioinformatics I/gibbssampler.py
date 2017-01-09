from time import time
from random import seed
from random import randrange
import numpy
import copy

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

def ProfileMostProbable(text,k,matrix):
	key = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
	kmers = []
	for i in range(len(text)-k+1):
		kmers.append(text[i:i+k])
	scores = {}
	for kmer in kmers:
		score = 1.0
		for i in range(len(kmer)):
			score *= (matrix[key[kmer[i]]][i])
		scores[kmer] = score
	thresh = 0.0
	result = text[:k]
	for item in scores:
		if (scores[item] > thresh):
			thresh = scores[item]
			result = item
	return result

def Profile(dna,k):
	key = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
	profile = [[1.0]*k,[1.0]*k,[1.0]*k,[1.0]*k]
	for seq in dna:
		for w in range(len(seq)):
			profile[key[seq[w]]][w] += 1
		for z in range(4):
			for x in range(k):
				profile[z][x] /= (len(dna)+4)
	return profile

def ProfileRandom(dna,k):
	matrix = Profile(dna,k)
	key = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
	kmers = []
	for i in range(len(dna)-k+1):
		kmers.append(dna[i:i+k])
	prob = []
	for kmer in kmers:
		score = 1.0
		for i in range(len(kmer)):
			score *= (matrix[key[kmer[i]]][i])
		prob.append(score)
	word = numpy.random.choice(kmers,1,prob)
	return word[0]

def GibbsSampler(dna,k,t,n):
	seed(time())
	Motifs = []
	for each in dna:
		start = randrange(len(each)-k+1)
		Motifs.append(each[start:start+k])
	BestMotifs = Motifs
	for j in range(1,n+1):
		i = randrange(t)
		Motifs2 = Motifs[:i] + Motifs[i+1:]
		ProfileMatrix = Profile(Motifs2,k)
		Motifs[i] = ProfileRandom(dna[i],k)
		if (Score(Motifs) < Score(BestMotifs)):
			BestMotifs = Motifs
	return BestMotifs

dna = ['CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA','GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG','TAGTACCGAGACCGAAAGAAGTATACAGGCGT','TAGATCAAGTTTCAGGTGCACGTCGGTGAACC','AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
ans = GibbsSampler(dna,8,5,100)
samp = ['TCTCGGGG','CCAAGGTG','TACAGGCG','TTCAGGTG','TCCACGTG']

for n in range(500):
	two = GibbsSampler(dna,8,5,100)
	if (Score(two) < Score(ans)):
		ans = two

print ans
print "Ans:" ,Score(ans)
print "Sample: ",Score(samp)
