import os, sys

dirs = os.listdir(sys.argv[1])
isTagalog = False
for textfilename in dirs:
	textfile = open(sys.argv[1] + textfilename, 'r')
	for line in textfile:
		if line.split().count('ng') > 0:
			isTagalog = True
			break
	if not isTagalog: print textfilename
	isTagalog = False
