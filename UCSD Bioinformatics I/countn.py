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

def count_n(t,p,n):
	ind = ApproximatePatternMatching(p,t,n)
	return len(ind)

print count_n('CATGCCATTCGCATTGTCCCAGTGA','CCC',2)