import sys

for arg in sys.argv[1:]:
	posfile = open(arg)
	sent = []
	for line in posfile:
		splitline = line.split()
		if len(splitline) == 0: 
			print ' '.join(sent)
			sent = []
			continue
		word = splitline[1]
		id = splitline[0]
		head = splitline[8]
		if word != '_':
			sent.append(head+'-'+id)
