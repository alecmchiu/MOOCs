def ApproximatePatternMatching(pattern,text,d):
	index = []
	for i in range(len(text)-len(pattern)+1):
		mismatches = 0
		for j in range(len(pattern)):
			if (pattern[j] != text[i+j]):
				mismatches += 1		
		if (mismatches <= d):
			index.append(i)
	return index

input = open('test.txt','r')
t = input.read().rstrip()
input.close()

p = 'CTCACGAAGAC'
d = 4
ind = ApproximatePatternMatching(p,t,d)

output = open('ApproximatePatternMatching.txt','w')
output.write(' '.join(map(str,ind)))
output.close()
