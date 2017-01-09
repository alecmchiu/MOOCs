def pattern_match(pattern,genome):
	index = []
	for i in range(len(genome)-len(pattern)):
		if (genome[i:i+len(pattern)] == pattern):
			index.append(i)
	return index

filename = "Vibrio_cholerae.txt"

input = file(filename,"r")
g = input.read().rstrip()
p = 'CTTGATCAT'

output = file("pattern_match_output.txt","w")
output.write(" ".join(map(str,pattern_match(p,g))))
output.close()