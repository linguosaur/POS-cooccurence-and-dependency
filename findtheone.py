import sys

#biemfile = open(sys.argv[1], 'r')
#for line in biemfile:
#	splitline = line.split()
#	for word in splitline:
#		print word

biemfile = open(sys.argv[1], 'r')
stdfile = open(sys.argv[2], 'r')

wordnum = 0
for stdline in stdfile:
	stdword = stdline.split('\t')[0]
	wordnum += 1
	biemword = biemfile.readline().strip()
	if biemword != stdword:
		print 'misalignment at word ' + repr(wordnum) + ' in stdfile:'
		print 'In standard: ' + stdword
		print 'In Biemann: ' + biemword
		continue
