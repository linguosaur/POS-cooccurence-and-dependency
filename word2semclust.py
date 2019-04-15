import re, sys


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
	splitCodeStr = splitStrLength*[""]

	for key in semClusters.keys():
		splitKey = key.split()
		splitKeyLength = len(splitKey)
		code = codeSeparatorChar.join(semClusters[key])
		if len(splitKey) > 1:
			replacement = [phraseStartChar] + (splitKeyLength-2)*[phraseMidChar] + [phraseEndChar+code]
		else:
			replacement = [code]

		for i in range(splitStrLength-splitKeyLength):
			if splitKey == splitStr[i:i+splitKeyLength] and replaceable(splitCodeStr[i:i+splitKeyLength]):
				splitCodeStr[i:i+splitKeyLength] = replacement

	return splitCodeStr


phraseStartChar = '<'
phraseMidChar = '-'
phraseEndChar = '>'
codeSeparatorChar = '/'

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
			print ' '.join(clustSent)
			sent = []
			continue
		splitline = line.split('\t')
		pos = splitline[3]
		if pos.startswith("NNP"):
			word = splitline[1].lower()
		else:
			word = splitline[2] # already lowercase
		sent.append(word)
