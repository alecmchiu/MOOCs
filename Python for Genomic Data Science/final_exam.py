filename = raw_input("File name:")
file = open(filename,"r")

sequences = {}

for line in file:
	line = line.rstrip()
	if line[0] == '>':
		words = line.split()
		name = words[0][1:]
		sequences[name] = ''
	else:
		sequences[name] = sequences[name] + line

file.close()

print
print "***There are %d sequences in the file.****" % len(sequences)
print

for key in sequences:
	print key

print
print "***Lengths***"
longest_key = ''
longest_value = 0
shortest_key = ''
shortest_value = 999999999
for key in sequences:
	if len(sequences[key]) > longest_value:
		longest_value = len(sequences[key])
		longest_key = key
	if len(sequences[key])  < shortest_value:
		shortest_value = len(sequences[key])
		shortest_key = key
print "Shortest:", shortest_key,":",shortest_value
print "Longest:",longest_key,":",longest_value 
print

def orf(seq, number):
	stop_codons = ['TAA','TAG','TGA']
	for id in seq:
		frames = {}
		pos = number - 1
		for i in range(pos,len(seq[id]),3):
			if (seq[id][i:i+3] == 'ATG'):
				start = i
				for j in range (start,len(seq[id]),3):
					if (seq[id][j:j+3] in stop_codons):
						frames[start] = j
						break
		print longest_orf(frames)
	return frames

def longest_orf(dict):
	start = 0
	stop = 0
	longest_length = 0
	for item in dict:
		length = dict[item] - item
		if length > longest_length:
			longest_length = length
			start = item
			stop = dict[item]
	return start, stop, longest_length

def kmer_index(seq, k):
	index = {}
	for read in seq:
		start = 0
		while (start < len(seq[read])-k):
			k_mer = seq[read][start:start+k]
			if k_mer not in index:
				index[k_mer] = 1
			else:
				index[k_mer] += 1
			start += 1
	return index

def frequent_kmer(index):
	dict = {}
	kmer = ''
	frequency = 0
	for seq in index:
		if index[seq] > frequency:
			kmer = seq
			frequency = index[seq]
	for seq in index:
		if index[seq] == frequency:
			dict[seq] = frequency
	return dict

orf(sequences,1)