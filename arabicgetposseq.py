import codecs, re, sys

for arg in sys.argv[1:]:
	posfile = codecs.open(arg, 'r', 'utf-8')
	sent = []
	re.U
	for line in posfile:
		splitline = line.split()
		if len(splitline) == 0: 
			print ' '.join(sent)
			sent = []
			continue
		pos = splitline[3]
		sent.append(pos)
