import sys

endwords = ['.', '?', '!']
suppendwords = ['CLOSE"', 'CLOSE\'', ']', ')']

option = sys.argv[1]
textfile = open(sys.argv[2])

seenEndword = False
for line in textfile:
	line = line.rstrip()
	splitline = line.split('\t')
	if len(splitline) >= 2:
		pinyin = splitline[0]

		if pinyin in endwords: 
			seenEndword = True
		elif seenEndword and pinyin not in suppendwords:
			print
			seenEndword = False
		
		if option == '-b':
			print pinyin,
		elif option == '-c':
			print pinyin
	else:
		print
		seenEndword = False
