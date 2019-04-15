import re, sys

posdict = {}
words = 0
for arg in sys.argv[1:]:
	thefile = open(arg, 'r')
	for line in thefile:
		splitline = line.split('\t')
		if len(splitline) > 4:
			words += 1
			word = splitline[1]
			coarsePOS = splitline[3]
			if splitline[1] not in posdict:
				# splitline[3] for coarsePOS, splitline[4] for finePOS
				posdict[word] = set(coarsePOS)
			else:
				posdict[word].add(coarsePOS)

print 'len(posdict): ', len(posdict)
print 'words: ', words
for k, v in posdict.iteritems():
	print k, '\t', ', '.join(v)
