def skew(i, string):
	guanine = 0
	cytosine = 0
	slice = string[0:i]
	guanine = slice.count('G')
	cytosine = slice.count('C')
	return guanine - cytosine


s = "CATTCCAGTACTTCATGATGGCGTGAAGA"

ls = []

for i in range(len(s)):
	ls.append(skew(i,s))

maximum = max(ls)

pos = []

for i in range(len(ls)):
	if (ls[i] == maximum):
		pos.append(i)

print pos


# for file input
"""
input = open('dataset_7_6.txt','r')
s = input.read().rstrip()
input.close()

ls = []
for i in range(len(s)):
	ls.append(skew(i,s))

minimum = min(ls)

pos = []

for i in range(len(ls)):
	if (ls[i] == minimum):
		pos.append(i)

output = open('skew.txt','w')
output.write(' '.join(map(str,pos)))
output.close()
"""