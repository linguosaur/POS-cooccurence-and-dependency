import math, re, sys

pairs = {}
wordTotals = {}
maxCooccurDiff = 0 
maxCooccurSame = 0
totalPairs = 0

inputfile = open(sys.argv[1])
for line in inputfile:
	splitline = re.sub('[<>\-_]', '', line).split() # ignore the unknown codes

	lineLength = len(splitline)
	if lineLength % 2 == 0: maxCooccurDiff += lineLength * lineLength / 4
	elif lineLength % 2 != 0: maxCooccurDiff += lineLength/2 * (lineLength/2 + 1)
	maxCooccurSame += lineLength * (lineLength - 1) / 2
	for i in range(lineLength-1):
		for j in range(i+1, lineLength):
			words_i = splitline[i].split('/')
			words_j = splitline[j].split('/')
			for wi in words_i:
				if wi in pairs:
					for wj in words_j:
						if wj in pairs[wi]:
							pairs[wi][wj] += 1
						else:
							pairs[wi][wj] = 1
					wordTotals[wi] += 1
				else:
					for wj in words_j:
						pairs[wi] = {wj: 1}
						wordTotals[wi] = 1
			for wj in words_j:
				if wj in pairs:
					for wi in words_i:
						if wi in pairs[wj]:
							pairs[wj][wi] += 1
						else:
							pairs[wj][wi] = 1
					wordTotals[wj] += 1
				else:
					for wi in words_i:
						pairs[wj] = {wi: 1}
						wordTotals[wj] = 1
			totalPairs += 1

for wordi in pairs:
	stats = {}
	si = {}
	print wordi, ':'
	keys = pairs[wordi].keys()
	for wordj in keys:
		cooccurence = 0.0
		if wordi == wordj: cooccurence = 1.0 * pairs[wordi][wordj] / maxCooccurSame
		else: cooccurence = 1.0 * pairs[wordi][wordj] / maxCooccurDiff
		# raw count, cooccurence, P(wordj|wordi), SI(wordi, wordj)
		stats[wordj] = [pairs[wordi][wordj]]
		stats[wordj].append(cooccurence)
		stats[wordj].append(1.0 * pairs[wordi][wordj] / wordTotals[wordi])
		si[wordj] = math.log(1.0 * totalPairs * pairs[wordi][wordj] / (wordTotals[wordi]*wordTotals[wordj]), 2)
	keys.sort(key=si.get)
	keys.reverse()
	for wordj in keys:
		sys.stdout.write('\t' + wordj)
		for stat in stats[wordj]:
			sys.stdout.write('\t' + repr(stat))
		print '\t' + repr(si[wordj])
	print 'total: ', wordTotals[wordi]
	print
print 'total pairs: ', totalPairs
