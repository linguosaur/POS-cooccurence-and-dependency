import os, os.path, re, sys

def extracttxt(textfilename):
	textfile = open(textfilename, 'r')
	for line in textfile:
		line = re.sub(r'<[^>]*>', '', line.rstrip())
		if line != '': print line

if os.path.isdir(sys.argv[1]):
	for textfilename in os.listdir(sys.argv[1]):
		extracttxt(textfilename)
else:
	extracttxt(sys.argv[1])
