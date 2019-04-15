import codecs, os, os.path, re, sys

def convertpy(textfilename):
	endlinetags = ['</HEADLINE>', '</DATELINE>', '</P>']

	textfile = codecs.open(textfilename, encoding='utf-8')
	for line in textfile:
		line = line.strip()
		if line[0] == '<' and line[-1] == '>':
			if line in endlinetags: print
			continue
		splitline = line.split()
		for taggedword in splitline:
			splittaggedword = taggedword.rstrip(')').rsplit('(', 1)
			word = splittaggedword[0]
			tag = splittaggedword[1]
			pinyin = ''
			for char in word:
				if char in dict:
					pinyin += dict[char]
				elif char.encode('utf-8') in puncdict:
					pinyin += puncdict[char.encode('utf-8')]
				else:
					try:
						pinyin += char.decode('utf-8').encode('ascii', 'strict')
					except:
						pinyin += 'UNK'
			
			print pinyin + '\t' + tag

dict = {}
puncdict = {'\xEF\xBC\x8C':',', '\xEF\xB9\x90':',', '\xE3\x80\x82':'.', '\x28':'(', '\x29':')', '\xE3\x80\x81':'PAUSE', '\xEF\xBC\x9A':':', '\xEF\xBC\x9B':';', '\xEF\xB9\x94':';', '\xE3\x80\x8C':'OPEN"', '\xE3\x80\x8D':'CLOSE"', '\xEF\xB9\x83':'OPEN"', '\xEF\xB9\x84':'CLOSE"', '\xEF\xBC\x88':'[', '\xEF\xBC\x89':']', '\xEF\xBC\x9F':'?', '\xEF\xBC\x81':'!', '\xEF\xBC\x8D':'-', '\xE2\x80\xA7':'DOT', '\xEF\xBC\x8E':'DOT', '\xE3\x80\x8E':'OPEN\'', '\xE3\x80\x8F':'CLOSE\'', '\xEF\xBD\x9C':'|', '\xE2\x80\xA6':'...'}
#worddictfile = codecs.open(sys.argv[1], encoding='utf-8')
#for line in worddictfile:
#	if line[0] == '#': continue
#	tradword = line.split()[0]
#	pinyin = re.split('[\[\]]', line)[1]
#	if tradword not in dict:
#		dict[tradword] = pinyin.replace(' ', '')
#worddictfile.close()

chardictfile = codecs.open(sys.argv[1], encoding='utf-8')
for line in chardictfile:
	if line[0] == '#': continue
	splitline = line.split()
	if len(splitline) >= 2:
		char = splitline[0]
		pinyin = splitline[1]
		if char not in dict:
			dict[char] = pinyin

textFileOrDir = sys.argv[2]
if os.path.isdir(textFileOrDir):
	for textfilename in os.listdir(textFileOrDir):
		convertpy(textFileOrDir + textfilename)
else:
	convertpy(textFileOrDir)
