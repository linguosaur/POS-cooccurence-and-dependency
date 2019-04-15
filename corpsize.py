import string, sys

def cooccurence(poslines):
	pairs = {}
	wordTotals = {}
	maxCooccurDiff = 0 
	maxCooccurSame = 0
	totalPairs = 0
	
	for line in poslines:
		splitline = line.split()
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
		keys = pairs[wordi].keys()
		keys.sort(key=pairs[wordi].get)
		keys.reverse()
		for wordj in keys:
			cooccurence = 0.0
			if wordi == wordj: cooccurence = 1.0 * pairs[wordi][wordj] / maxCooccurSame
			else: cooccurence = 1.0 * pairs[wordi][wordj] / maxCooccurDiff
			# raw count, cooccurence, P(wordj|wordi)
			pairs[wordi][wordj] = [pairs[wordi][wordj], cooccurence, 1.0 * pairs[wordi][wordj]/wordTotals[wordi]]
	
	return pairs


def addpair (key1, key2, dict):
	if key1 in dict:
		if key2 in dict[key1]:
			dict[key1][key2] += 1
		else:
			dict[key1][key2] = 1
	else:
		dict[key1] = {key2: 1}

def compare2(deplines, poslines, stats):
	depsstats = 3*[0.0]
	nodepsstats = 3*[0.0]
	totalDeps = 0
	splitposlines = []
	
	for line in poslines:
		splitposlines.append(line.split())
	
	setOfAll = set()
	for pos1 in stats:
		for pos2 in stats[pos1]:
			setOfAll.add(pos1+' '+pos2)
	
	setOfDeps = set()
	deps = {}
	for line_i in range(len(deplines)):
		splitdepline = deplines[line_i].split()
		splitposline = splitposlines[line_i]
		totalDeps += len(splitdepline)
		for dep in splitdepline:
			splitdep = dep.split('-')
			headi = string.atoi(splitdep[0])
			argi = string.atoi(splitdep[1])
			if headi > 0:
				headpos = splitposline[headi-1]
				argpos = splitposline[argi-1]
				setOfDeps.add(headpos+' '+argpos)
				addpair(headpos, argpos, deps)
	
	setOfNoDeps = setOfAll - setOfDeps
	
	totalDepPairs = 0
	for pospair in setOfDeps:
		splitpospair = pospair.split()
		head = splitpospair[0]
		arg = splitpospair[1]
		depsstats[0] += stats[head][arg][1]
		depsstats[1] += stats[head][arg][2]
		depsstats[2] += stats[arg][head][2]
		totalDepPairs += 1
	for i in range(len(depsstats)):
		depsstats[i] /= totalDepPairs
	
	totalNoDepPairs = 0
	for pospair in setOfNoDeps:
		splitpospair = pospair.split()
		head = splitpospair[0]
		arg = splitpospair[1]
		nodepsstats[0] += stats[head][arg][1]
		nodepsstats[1] += stats[head][arg][2]
		nodepsstats[2] += stats[arg][head][2]
		totalNoDepPairs += 1
	for i in range(len(nodepsstats)):
		nodepsstats[i] /= totalNoDepPairs
	
	for stat in depsstats: print stat, '\t',
	for stat in nodepsstats: print stat, '\t',
	print

depfile = open(sys.argv[1], 'r')
posfile = open(sys.argv[2], 'r')
deplines = depfile.readlines()
poslines = posfile.readlines()
depfile.close()
posfile.close()

for linenum in range(1, len(poslines)+1):
	print linenum, '\t',
	stats = cooccurence(poslines[0:linenum])
	compare2(deplines[0:linenum], poslines[0:linenum], stats)
