def PatternCount(text,pattern):
	count = 0
	for i in range(len(text) - len(pattern)):
		if text[i:i+len(pattern)] == pattern:
			count += 1
	return count

t = raw_input("Text: ")
p = raw_input("Pattern: ")

print PatternCount(t,p)