from collections import defaultdict

def DeBruijn3(patterns):
	output = open('debruijn3.txt','w')
	dict = defaultdict(list)
	for each in patterns:
		dict[each[:-1]].append(each[1:])
	for each in sorted(dict):
		string = each + ' -> '
		for item in dict[each]:
			string = string + item + ','
		output.write(string[:-1])
		output.write('\n')
	output.close()
	return

"""
def DeBruijn3(patterns):
	dict = defaultdict(list)
	for each in patterns:
		dict[each[:-1]].append(each[1:])
	for each in sorted(dict):
		string = each + ' -> '
		for item in dict[each]:
			string = string + item + ','
		print string[:-1]
	return

patt = ['GAGG','CAGG','GGGG','GGGA','CAGG','AGGG','GGAG']
DeBruijn3(patt)
"""

input = open('dataset_200_7.txt','r')
kmers = []
for line in input:
	kmers.append(line.rstrip())
input.close()
DeBruijn3(kmers)