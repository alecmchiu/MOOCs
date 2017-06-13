#!/bin/env python3

cases = ['azcbobobegghakl','abcbcd','zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyz']

s = cases[2]

start = 0
end = 0
length = 0
longest_start = 0
longest_end = 1
longest_length = 0

for i in range(len(s)-1):
	if s[i+1] >= s[i]:
		end = i+2
		length += 1
		if i == len(s)-2:
			if length > longest_length:
				longest_length = length
				longest_start = start
				longest_end = end
	else:
		if length > longest_length:
			longest_length = length
			longest_start = start
			longest_end = end
		start = i+1
		length = 0
		end = i+2

print("Longest substring in alphabetical order is: {}".format(s[longest_start:longest_end]))