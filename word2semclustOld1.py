import re, sys

def extendable(splitInitWords, splitStr):
	if len(splitInitWords) < len(splitStr) and splitStr[:len(splitInitWords)] == splitInitWords:
		return True
	else:
		return False

def lookupWord(word):
	if words[i] in semClusters:
		return '/'.join(semClusters[words[i]])
	else:
		return "UNK"

def words2semClustsold(words):
	clustSent = []
	wordBuffer = []
	clustBuffer = []
	for i in range(len(words)):
		extend = False
		wordBuffer.append(words[i])
		clust4wordsi = lookupWord(words[i])

		joinedWordBuffer = ' '.join(wordBuffer)
		if len(wordBuffer) > 1 and joinedWordBuffer in semClusters:
			clustBuffer = len(clustBuffer)*['_'] + ['/'.join(semClusters[joinedWordBuffer])]
		else:
			clustBuffer.append(clust4wordsi)

		for key in semClusters.keys():
			if extendable(wordBuffer, key.split()):
				extend = True
				break

		if not extend:
			clustSent += clustBuffer
			wordBuffer = []
			clustBuffer = []
			for key in semClusters.keys():
				if extendable([words[i]], key.split()):
					wordBuffer = [words[i]]
					clustBuffer = [clust4wordsi]
					break

	return clustSent


def phraseEndCode(code):
	if len(code) > 1 and code[0] == phraseEndChar:
		return True

	return False

def normalCode(code):
	if len(code) > 1 and code[0] != phraseEndChar:
		return True

	return False

def replaceable(codeWindow):
	if (codeWindow[0] == phraseStartChar or normalCode(codeWindow[0])) and len(codeWindow[-1]) > 1:
		return True
	if codeWindow[0] == "" and (codeWindow[-1] == "" or len(codeWindow[-1]) > 1):
		return True
	if (codeWindow[0] == phraseStartChar or normalCode(codeWindow[0])) and codeWindow[-1] == "":
		return True

	return False

def words2semClusts(splitStr):
	splitStrLength = len(splitStr)
	unknowns = range(splitStrLength)
	splitCodeStr = splitStrLength*[""]

	for key in semClusters.keys():
		splitKey = key.split()
		splitKeyLength = len(splitKey)
		code = '/'.join(semClusters[key])
		if len(splitKey) > 1:
			replacement = [phraseStartChar] + (splitKeyLength-2)*[phraseMidChar] + [phraseEndChar+code]
		else:
			replacement = [code]

		# print "replacement:", replacement

		for i in range(splitStrLength-splitKeyLength):
			if splitKey == splitStr[i:i+splitKeyLength] and replaceable(splitCodeStr[i:i+splitKeyLength]):
				splitCodeStr[i:i+splitKeyLength] = replacement

	return splitCodeStr


phraseStartChar = '<'
phraseMidChar = '_'
phraseEndChar = '>'

# build table for lookup
clusterfile = open(sys.argv[1])
semClusters = {}
clusterCode = ""
for line in clusterfile:
	if line[0] == '(':
		if line[1] == '"':
			clusterCode = re.split('[<>]', line)[1].split()[0]
	elif line[0] != ')':
		word = line.split('\t')[0]
		word = word.strip('"').lower()
		if word in semClusters:
			semClusters[word].append(clusterCode)
		else:
			semClusters[word] = [clusterCode]

sent = []
clustSent = []
for arg in sys.argv[2:]:
	parsefile = open(arg)
	for line in parsefile:
		if line.strip() == '':
			clustSent = words2semClusts(sent)
			#print "sent:", ' '.join(sent)
			#print ' '.join(clustSent)
			for i in range(len(sent)):
				print sent[i] + '\t' + clustSent[i]
			sent = []
			continue
		splitline = line.split('\t')
		pos = splitline[3]
		if pos.startswith("NNP"):
			word = splitline[1].lower()
		else:
			word = splitline[2] # already lowercase
		if word != "_":
			sent.append(word)
