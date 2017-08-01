#!/usr/bin/env python3

def cipher(map_from, map_to, code):
	key = {}
	for i in range(len(map_from)):
		key[map_from[i]] = map_to[i]
	encrypted = []
	for character in code:
		encrypted.append(key[character])
	return (key, ''.join(encrypted))

if __name__ == '__main__':
	print(cipher("abcd","dcba","dab"))