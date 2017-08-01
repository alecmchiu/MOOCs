#!/usr/bin/env python3

def max_val(t):
	current = float("-inf")
	for each in t:
		if type(each) == tuple or type(each) == list:
			num = max_val(each)
			if num > current:
				current = num
		else:
			if each > current:
				current = each
	return current

if __name__ == "__main__":
	print(max_val2((5, (1,2), [[1],[2]])))
	print(max_val2((5, (1,2), [[1],[9]])))