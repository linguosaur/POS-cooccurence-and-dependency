import codecs, re, sys

posdict = {}
for arg in sys.argv[1:]:
	posfile = codecs.open(arg, 'r', 'utf-8')
	read = False
	sent = ''
	re.U
	for line in posfile:
		sent = sent.strip()
		if re.search('<S ID=\d+>', line): read = True
		elif re.search('</S>', line): 
			splitsent = sent.split()
			for pair in splitsent:
				splitpair = pair.split('_')
				if splitpair[0] not in posdict:
					posdict[splitpair[0]] = set([splitpair[1]])
				else:
					posdict[splitpair[0]].add(splitpair[1])
			sent = ''
			read = False
		elif read: sent += line

print 'len(posdict): ', len(posdict)
for k, v in posdict.iteritems():
	print k.encode('utf-8'), '\t'.encode('utf-8'), ', '.join(v).encode('utf-8')
