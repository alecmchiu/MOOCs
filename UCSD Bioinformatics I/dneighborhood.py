def HammingDistance(p,q):
	distance = 0
	for i in range(len(p)):
		if (p[i] != q[i]):
			distance += 1
	return distance

def ImmediateNeighbors(pattern):
	alphabet = ['A','T','C','G']
	Neighborhood = set()
	for i in range(len(pattern)):
		symbol = pattern[i]
		for nt in alphabet:
			if (nt != symbol[i]):
				Neighbor = pattern[:i] + nt + pattern[i+1:]
				Neighborhood.add(Neighbor)
	return Neighborhood

def Neighbors(pattern,d):
	alphabet = ['A','T','C','G']
	if (d == 0):
		return set([pattern])
	if (len(pattern) == 1):
		return set(alphabet)
	Neighborhood = set()
	SuffixNeighbors = Neighbors(pattern[1:],d)
	for each in SuffixNeighbors:
		if (HammingDistance(pattern[1:], each) < d):
			for nt in alphabet:
				Neighborhood.add(nt + each)
		else:
			Neighborhood.add(pattern[0] + each)
	return Neighborhood

def IterativeNeighbors(pattern,d):
	Neighborhood = set([pattern])
	for j in range(1,d):
		for each in Neighborhood:
			Neighborhood.add(ImmediateNeighbors(each))
	return Neighborhood

"""
ls = Neighbors('TGCTCAATCG',2)

output = open('dneighborhood.txt','w')
for each in ls:
	output.write(each)
	output.write('\n')

output.close()
"""

ls = Neighbors('CCCC',3)
print len(ls)