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

from time import time
from random import seed
from random import randrange

def RandomizedMotifSearch(dna,k,t):
	seed(time())
	Motifs = ['TGA','GTT','GAA','TGT']
	"""
	Motifs = []
	for each in dna:
		start = randrange(len(each)-k+1)
		Motifs.append(each[start:start+k])
	"""
	BestMotifs = Motifs
	while (True):
		ProfileMat = Profile(Motifs,k)
		Motifs2 = []
		for each in dna:
			Motifs2.append(ProfileMostProbable(each,k,ProfileMat))
		Motifs = Motifs2
		if (Score(Motifs) < Score(BestMotifs)):
			BestMotifs = Motifs
		else:
			return BestMotifs

seqs = ['TGACGTTC','TAAGAGTT','GGACGAAA','CTGTTCGC']
ans = RandomizedMotifSearch(seqs,3,4)

print ' '.join(map(str,ans))