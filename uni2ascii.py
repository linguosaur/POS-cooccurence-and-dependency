import sys, codecs, re

dictfile = codecs.open(sys.argv[1], 'r', 'utf-8')

ipa2ascii = {}
for line in dictfile:
    splitline = line.lstrip(unicode(codecs.BOM_UTF8, 'utf-8')).rstrip('\r\n').split('\t')
    if len(splitline) < 2: print splitline
    else: ipa2ascii[splitline[0]] = splitline[1]
dictfile.close()
# print ipa2ascii
# print "length: " + repr(len(ipa2ascii))

textfile = codecs.open(sys.argv[2], 'r', 'utf-8')

for line in textfile:
    line = re.sub(u'\ufeff', '', line)
    #if line.find(u'\xe1') != -1: print "line: " + repr(line)
    for ipa in ipa2ascii.iterkeys():
        line = re.sub(re.escape(ipa), ipa2ascii[ipa], line)
    print line.encode('ascii'),
textfile.close()
