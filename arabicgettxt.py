import codecs, sys

sent = []
for arg in sys.argv[1:]:
	posfile = codecs.open(arg, 'r', 'utf-8')
	for line in posfile:
		if line.strip() == '':
			print ' '.join(sent).encode('utf-8')
			sent = []
			continue
		splitline = line.split('\t')
		word = splitline[1].split('_')[1]
		if word.strip() == '': word = '_'
		sent.append(word)
