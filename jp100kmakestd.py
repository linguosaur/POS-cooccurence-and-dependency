import codecs, sys

option = sys.argv[1]
inputfile = codecs.open(sys.argv[2], 'r', 'utf-8')
for line in inputfile:
	splitline = line.split('\t')
	if len(splitline) > 4:
		if option == '-c': # coarse
			splitpos = splitline[3].split('-')
			out = splitline[0] + '\t' + splitpos[0]
		elif option == '-f': # fine
			out = splitline[0] + '\t' + splitline[3]
		print out.encode('utf-8')
