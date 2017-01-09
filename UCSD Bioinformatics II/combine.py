def combine(ls):
	combined = ls[0]
	for i in range(1,len(ls)):
		combined = combined + ls[i][-1]
	return combined

"""
it = ['ACCGA','CCGAA','CGAAG','GAAGC','AAGCT']
print combine(it)
"""

ls = []
input = open('dataset_198_3.txt','r')
for line in input:
	ls.append(line.rstrip())
input.close()

output = open('combine.txt','w')
output.write(combine(ls))
output.close()