def DeBruijn(k,text):
	kmers = []
	for i in range(len(text) - k + 1):
		kmers.append(text[i:i+k])
	k1mers = set()
	for item in kmers:
		k1mers.add(item[:-1])
	k1mers = list(k1mers)
	k1mers.sort()
	for each in k1mers:
		string = each + ' -> '
		for item in kmers:
			if (each[1:] == item[:-2]):
				string = string + item[:-1] + ','
		print string[:-1]
	return

DeBruijn(4,'AAGATTCTCTAAGA')
