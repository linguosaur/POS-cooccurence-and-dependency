import codecs, re, sys

posdict = {}
words = 0
for arg in sys.argv[1:]:
	thefile = codecs.open(arg, 'r', 'utf-8')
	for line in thefile:
		splitline = line.split('\t')
		if len(splitline) > 4:
			words += 1
			word = splitline[1].split('_')[1]
			if word.strip() == '': word = '_'
			coarsePOS = splitline[3]
			if splitline[1] not in posdict:
				# splitline[3] for coarsePOS, splitline[4] for finePOS
				posdict[word] = set(coarsePOS)
			else:
				posdict[word].add(coarsePOS)

for k, v in posdict.iteritems():
	print k.encode('utf-8'), '\t'.encode('utf-8'), ', '.join(v).encode('utf-8')
