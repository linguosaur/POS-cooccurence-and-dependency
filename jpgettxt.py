import sys

sent = []
for arg in sys.argv[1:]:
	posfile = open(arg, 'r')
	for line in posfile:
		if line.strip() == '':
			print '\n'.join(sent)
			print
			sent = []
			continue
		splitline = line.split('\t')
		sent.append(splitline[1])
