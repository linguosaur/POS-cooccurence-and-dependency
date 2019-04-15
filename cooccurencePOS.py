import math, sys

pairs = {}
wordTotals = {}
maxCooccurDiff = 0 
maxCooccurSame = 0
totalPairs = 0

inputfile = open(sys.argv[1])
for line in inputfile:
	splitline = line.split()
	while '_' in splitline:
		splitline.remove('_')
	lineLength = len(splitline)
	if lineLength % 2 == 0: maxCooccurDiff += lineLength * lineLength / 4
	elif lineLength % 2 != 0: maxCooccurDiff += lineLength/2 * (lineLength/2 + 1)
	maxCooccurSame += lineLength * (lineLength - 1) / 2
	for i in range(lineLength-1):
		for j in range(i+1, lineLength):
			wordi = splitline[i]
			wordj = splitline[j]
			if wordi in pairs:
				wordTotals[wordi] += 1
				if wordj in pairs[wordi]:
					pairs[wordi][wordj] += 1
				else:
					pairs[wordi][wordj] = 1
			else:
				pairs[wordi] = {wordj: 1}
				wordTotals[wordi] = 1
			totalPairs += 1
			if wordj in pairs:
				wordTotals[wordj] += 1
				if wordi in pairs[wordj]:
					pairs[wordj][wordi] += 1
				else:
					pairs[wordj][wordi] = 1
			else:
				pairs[wordj] = {wordi: 1}
				wordTotals[wordj] = 1


for wordi in pairs:
	numPairs = {}
	cooccurences = {}
	percentagePairs = {}
	si = {}
	print wordi, ':'
	keys = pairs[wordi].keys()
	for wordj in keys:
		cooccurence = 0.0
		if wordi == wordj: cooccurence = 1.0 * pairs[wordi][wordj] / maxCooccurSame
		else: cooccurence = 1.0 * pairs[wordi][wordj] / maxCooccurDiff
		# raw count, cooccurence, P(wordj|wordi), SI(wordi, wordj)
		numPairs[wordj] = pairs[wordi][wordj]
		cooccurences[wordj] = cooccurence
		percentagePairs[wordj] = 1.0 * pairs[wordi][wordj] / wordTotals[wordi]
		si[wordj] = math.log(1.0 * totalPairs * pairs[wordi][wordj] / (wordTotals[wordi]*wordTotals[wordj]), 2)
	keys.sort(key=numPairs.get)
	keys.reverse()
	for wordj in keys:
		print '\t' + '\t'.join([wordj, repr(numPairs[wordj]), repr(cooccurences[wordj]), repr(percentagePairs[wordj]), repr(si[wordj])])
	print 'total: ', wordTotals[wordi]
	print
print 'total pairs: ', totalPairs
