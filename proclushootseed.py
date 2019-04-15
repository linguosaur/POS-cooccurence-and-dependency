import sys, codecs, re 

f = codecs.open(sys.argv[1], 'r', 'utf-8')
re.U
for line in f:
	utf8line = line.encode('utf-8')
	splitline = utf8line.split()
	print '\n'.join(splitline) + "\n"
