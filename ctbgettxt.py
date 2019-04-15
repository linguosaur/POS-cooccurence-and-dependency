import codecs, re, sys

sents = []
for arg in sys.argv[1:]:
	posfile = codecs.open(arg, 'r', 'utf-8')
	read = False
	sent = ''
	re.U
	for line in posfile:
		if re.search('<S ID=\d+>', line): read = True
		elif re.search('</S>', line):
			for word in sent.strip().split():
				print word.encode('utf-8')
#			for word in sent.strip().split():
#				for char in word:
#					print ord(char),
#				print
			print
			sent = ''
			read = False
		elif read: sent += line
