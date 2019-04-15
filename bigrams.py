import sys

bigrams = {}
mergedKeyBigrams = {}
totalBigrams = 0

inputfile = open(sys.argv[1])
for line in inputfile:
	splitline = line.lower().split()
	for i in range(len(splitline)-1):
		thisword = splitline[i]
		nextword = splitline[i+1]
		if thisword in bigrams:
			if nextword in bigrams[thisword]:
				bigrams[thisword][nextword] += 1
				mergedKeyBigrams[thisword+' '+nextword] += 1
			else:
				bigrams[thisword][nextword] = 1
				mergedKeyBigrams[thisword+' '+nextword] = 1
		else:
			bigrams[thisword] = {nextword: 1}
			mergedKeyBigrams[thisword+' '+nextword] = 1
		totalBigrams += 1

keys = mergedKeyBigrams.keys()
keys.sort(key=mergedKeyBigrams.get)
keys.reverse()
for wordpair in keys:
	print wordpair, '\t', 1.0 * mergedKeyBigrams[wordpair]/totalBigrams
