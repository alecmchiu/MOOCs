def HammingDistance(p,q):
	distance = 0
	for i in range(len(p)):
		if (p[i] != q[i]):
			distance += 1
	return distance

s = 'TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC'
q = 'GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA'

print HammingDistance(s,q)

