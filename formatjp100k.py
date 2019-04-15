import codecs, sys

inputfile = codecs.open(sys.argv[1], 'r', 'utf-8')
for line in inputfile:
	i = 0
	while i < len(line) and line[i] != '\t': i += 1
	print line[i+1:len(line)].encode('utf-8'),
