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
	result = ''
	for item in scores:
		if (scores[item] > thresh):
			thresh = scores[item]
			result = item
	return result

def myFloat(myList):
	return map(float,myList)

input = open('dataset_159_3.txt','r')

text = input.readline().rstrip()
k = int(input.readline().rstrip())
matrix_lines = []
for line in input:
	matrix_lines.append(line.rstrip())
matrix_str = [i.split(' ') for i in matrix_lines]

matrix = map(myFloat,matrix_str)

input.close()

print ProfileMostProbable(text,k,matrix)