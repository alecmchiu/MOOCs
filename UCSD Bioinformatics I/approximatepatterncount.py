def HammingDistance(p,q):
	distance = 0
	for i in range(len(p)):
		if (p[i] != q[i]):
			distance += 1
	return distance

def ApproximatePatternCount(text, pattern, d):
	count = 0
	for i in range(len(text)-len(pattern)+1):
		current_pattern = text[i:i+len(pattern)]
		if (HammingDistance(pattern,current_pattern) <= d):
			count += 1
	return count

print ApproximatePatternCount('','AAGCGA',2)