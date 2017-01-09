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

def GreedyMotifSearch(DNA, k, t):
	key = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
	best_motifs = []
	for strand in DNA:
		best_motifs.append(strand[:k])
	for i in range(len(DNA[0])-k+1):
		motif = []
		motif.append(DNA[0][i:i+k])
		for j in range(1,t):
			profile = [[0.0]*k,[0.0]*k,[0.0]*k,[0.0]*k]
			for seq in motif:
				for w in range(len(seq)):
					profile[key[seq[w]]][w] += 1
			for z in range(4):
				for x in range(k):
					profile[z][x] /= len(motif)
			motif.append(ProfileMostProbable(DNA[j],k,profile))
		if (Score(motif) < Score(best_motifs)):
			best_motifs = motif
	return best_motifs

def GreedyMotifSearch2(DNA, k, t):
	key = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
	best_motifs = []
	for strand in DNA:
		best_motifs.append(strand[:k])
	for i in range(len(DNA[0])-k+1):
		motif = []
		motif.append(DNA[0][i:i+k])
		for j in range(1,t):
			profile = [[1.0]*k,[1.0]*k,[1.0]*k,[1.0]*k]
			for seq in motif:
				for w in range(len(seq)):
					profile[key[seq[w]]][w] += 1
			for z in range(4):
				for x in range(k):
					profile[z][x] /= (len(motif)+4)
			motif.append(ProfileMostProbable(DNA[j],k,profile))
		if (Score(motif) < Score(best_motifs)):
			best_motifs = motif
	return best_motifs

input = open('rosalind_2dba.txt','r')
seq = []
for line in input:
	seq.append(line.rstrip())
input.close()

ans = GreedyMotifSearch(seq,12,25)

output = open('greedymotifsearch1.txt','w')
for item in ans:
	output.write(item)
	output.write('\n')

output.close()



