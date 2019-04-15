import sys, re

word2gloss = {}
textfile = open(sys.argv[1], 'r')
glossfile = open(sys.argv[2], 'r')

for textline in textfile:
	glossline = glossfile.readline()
	splittextline = textline.split()
	splitglossline = glossline.split()
	if len(splittextline) != len(splitglossline):
		print "textline: " + repr(textline)
		print "glossline: " + repr(glossline)
	for i in range(len(splittextline)):
		w = splittextline[i].strip()
		if w != '' and w not in word2gloss: 
			word2gloss[w] = splitglossline[i]

textfile.close()
glossfile.close()

wordfile = open(sys.argv[3], 'r')
for wordline in wordfile:
	if wordline.strip() != '': print word2gloss[wordline.strip()]
