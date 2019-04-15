import sys

posSent = []
for arg in sys.argv[1:]:
	parsefile = open(arg)
	for line in parsefile:
		if line.strip() == '':
			print ' '.join(posSent)
			posSent = []
			continue
		splitline = line.split('\t')
		word = splitline[1]
		pos = splitline[3]
		posSent.append(pos)
