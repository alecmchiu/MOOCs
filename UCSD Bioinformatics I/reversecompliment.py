def rc(pattern):
	complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
	t = ''
	for base in pattern:
		t = complement[base] + t
	return t

"""
input = open("dataset_3_2.txt","r")
p = input.read().rstrip()
input.close()
output = open("output.txt","w")
output.write(rc(p))
output.close()
"""
p = raw_input("Pattern: ")
print rc(p)