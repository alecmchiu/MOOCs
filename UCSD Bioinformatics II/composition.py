def composition(k, text):
	kmers = []
	for i in range(len(text)-k+1):
		kmers.append(text[i:i+k])
	return kmers

"""
ls = composition(5,'CAATCCAAC')
for each in ls:
	print each
"""

input = open('dataset_197_3.txt','r')
string = input.read().rstrip()
ls = composition(100,string)
input.close()

output = open('compositionoutput.txt','w')
for item in ls:
	output.write(item)
	output.write('\n')

output.close()
