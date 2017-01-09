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
	Motifs = []
	for each in dna:
		start = randrange(len(each)-k+1)
		Motifs.append(each[start:start+k])
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

input = open('rosalind_2fba.txt','r')
seq = []
for line in input:
	seq.append(line.rstrip())
input.close()

ans = RandomizedMotifSearch2(seq,15,20)
n = 0
tm = time()
while (n < 1000):
	two = RandomizedMotifSearch2(seq,15,20)
	if (Score(two) < Score(ans)):
		ans = two
	n += 1
length = time() - tm
print length

output = open('randomizedmotifsearch.txt','w')
for item in ans:
	output.write(item)
	output.write('\n')

output.close()

input = open('sample.txt','r')
samp = []
for line in input:
	samp.append(line.rstrip())
input.close

print "Sample:",Score(samp)
print "Ans:",Score(ans)