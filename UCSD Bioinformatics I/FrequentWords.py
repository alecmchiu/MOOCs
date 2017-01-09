def PatternCount(text,pattern):
	count = 0
	for i in range(len(text) - len(pattern)):
		if text[i:i+len(pattern)] == pattern:
			count += 1
	return count

def FrequentWords(text, k):
	FrequentPatterns = set()
	count = []
	for i in range(len(text) - k):
		pattern = text[i:i+k]
		count.append(PatternCount(text,pattern))
	maxCount = max(count)
	for i in range(len(text) - k):
		if count[i] == maxCount:
			FrequentPatterns.add(text[i:i+k])
	return FrequentPatterns

t = raw_input("Text: ")
k = int(raw_input("k: "))

print FrequentWords(t,k)
