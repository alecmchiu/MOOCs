def Universial3(numbers):
	nums = ['000','001','010','011','100','101','110','111']
	for each in numbers:
		found = True
		for item in nums:
			if (not (item in each)):
				found = False
		if (found):
			print each + "is 3-universal"
		else:
			print each + "is NOT 3-universal"
	return

numbs = ['0001110100','0011101000','1110001011','1001101100','1100011011','0101001101']

Universial3(numbs)