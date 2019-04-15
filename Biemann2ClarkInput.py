import re, sys

def stripPunc(string):
	newString = re.sub('[^\w\d\s]+(?=[\s$])', '', string)
	newString = re.sub('(?<=[\s^])[^\w\d\s]+', '', newString)
	newString = re.sub('_', '', newString)
	newString = re.sub('[^\w\d\.\'\-\s]', '', newString)
	newString = re.sub('(?<=\s)[\-](?=\s)', '', newString)
	return newString

textFile = open(sys.argv[1])
textFileLines = textFile.readlines()
textFile.close()

for line in textFileLines:
	splitline = stripPunc(line.lower()).rstrip().split()
	for word in splitline:
		print word
	print
