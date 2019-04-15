import sys

biemannfile = open(sys.argv[1], 'r')
for line in biemannfile:
	splitline = line.rstrip().split()
	for wordandpos in splitline:
		splitwordandpos = wordandpos.split('|')
		word = splitwordandpos[0]
		pos = splitwordandpos[1].rstrip('*')
		print word + '\t' + pos
