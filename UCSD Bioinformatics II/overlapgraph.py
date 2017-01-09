def OverlapGraph(ls):
	output = open('overlapgraph.txt','w')
	for each in ls:
		for item in ls:
			if (each[1:] == item[:-1]):
				output.write(each + " -> " + item)
				output.write('\n')
	output.close()
	return


#ls = ['ATGCG','GCATG','CATGC','AGGCA','GGCAT']

ls = []

input = open('dataset_198_9.txt','r')
for line in input:
	ls.append(line.rstrip())
input.close()

OverlapGraph(ls)