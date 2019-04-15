import os, sys

dirs = os.listdir(sys.argv[1])
isTagalog = False
for textfilename in dirs:
	textfile = open(sys.argv[1] + textfilename, 'r')
	print sys.argv[1] + textfilename + ":"
	for line in textfile:
		print line
	print
