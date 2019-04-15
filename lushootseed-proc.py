import sys, re, codecs

f = codecs.open(sys.argv[1], encoding='utf-16')
re.U
for line in f:
	line = u'line: ' + line
	print line.encode('utf-16'),
f.close()
