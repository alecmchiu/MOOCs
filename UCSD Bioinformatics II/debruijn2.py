from collections import defaultdict

def DeBruijn2(k,text):
	output = open('debruijn2.txt','w')
	dict = defaultdict(list)
	kmers = []
	for i in range(len(text)-k+1):
		kmers.append(text[i:i+k])
	for each in kmers:
		dict[each[:-1]].append(each[1:])
	for each in sorted(dict):
		string = each + ' -> '
		for item in dict[each]:
			string = string + item + ','
		output.write(string[:-1])
		output.write('\n')
	output.close()
	return

#DeBruijn2(4,'AAGATTCTCTAAGA')

input = open('dataset_199_6.txt','r')
string = input.read().rstrip()
input.close()

DeBruijn2(12,string)