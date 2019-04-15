import sys

parsefile = open(sys.argv[1])
insertFile = open(sys.argv[2])

sent = []
insertFileLine = insertFile.readline().rstrip()
insertFileLine = insertFileLine.replace('_', '-')
for line in parsefile:
	if line.strip() == '':
		for i in range(len(sent)):
			if sent[i] == '_':
				splitInsertLine = splitInsertLine[:i] + ['_'] + splitInsertLine[i:]
		print ' '.join(splitInsertLine)
		sent = []
		insertFileLine = insertFile.readline().rstrip()
		insertFileLine = insertFileLine.replace('_', '-')
		continue
	splitParseLine = line.split('\t')
	splitInsertLine = insertFileLine.split(' ')
	word = splitParseLine[1]
	sent.append(word)	
