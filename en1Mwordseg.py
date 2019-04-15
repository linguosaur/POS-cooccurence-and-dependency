import sys, operator

words = set()
prefixes = {}
suffixes = {}

wordsfile = open(sys.argv[1])
for line in wordsfile:
	words.add(line.strip().split('\t')[1])

for word in words:
	for char_i in range(1, len(word)):
		prefix = word[0:char_i]
		remaining = word[char_i:len(word)]
		if remaining in words:
			print prefix + '-', '+', remaining
			if prefix in prefixes:
				prefixes[prefix] += 1
			else:
				prefixes[prefix] = 1
	for char_i in range(len(word)-1, 0, -1):
		suffix = word[char_i:len(word)]
		remaining = word[0:char_i]
		if remaining in words:
			print remaining, '+', '-' + suffix
			if suffix in suffixes:
				suffixes[suffix] += 1
			else:
				suffixes[suffix] = 1

print '\nPrefixes:\n'
for item in sorted(prefixes.items(), key=operator.itemgetter(1), reverse=True):
	print item[0] + '\t' + repr(item[1])
print '\nSuffixes:\n'
for item in sorted(suffixes.items(), key=operator.itemgetter(1), reverse=True):
	print item[0] + '\t' + repr(item[1])
