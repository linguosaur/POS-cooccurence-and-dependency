import os, sys

filesfile = open(sys.argv[1], 'r')
srcdir = sys.argv[2]
destdir = sys.argv[3]
for line in filesfile:
	filename = line.strip()
	cmd = 'move ' + srcdir + filename + ' "' + destdir + '."'
	#print cmd,
	os.system(cmd)
