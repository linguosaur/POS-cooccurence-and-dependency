import math, sys

leftContexts = {}
rightContexts = {}
entropies = {}
leftwordFreqTotal = {}
rightwordFreqTotal = {}

# find left and right context distributions for each word
inputfile = open(sys.argv[1], 'r')
for line in inputfile:
		splitline = line.lower().split()
		splitline = ['<S>'] + splitline + ['</S>']
		for i in range(len(splitline)):
			thisword = splitline[i]
			if i > 0:
				leftword = splitline[i-1]
				if thisword in leftContexts:
					if leftword in leftContexts[thisword]:
						leftContexts[thisword][leftword] += 1
					else:
						leftContexts[thisword][leftword] = 1
					leftwordFreqTotal[thisword] += 1
				else:
					leftContexts[thisword] = {leftword: 1}
					leftwordFreqTotal[thisword] = 1
			if i < len(splitline)-1:
				rightword = splitline[i+1]
				if thisword in rightContexts:
					if rightword in rightContexts[thisword]:
						rightContexts[thisword][rightword] += 1
					else:
						rightContexts[thisword][rightword] = 1
					rightwordFreqTotal[thisword] += 1
				else:
					rightContexts[thisword] = {rightword: 1}
					rightwordFreqTotal[thisword] = 1

# identify dependencies
for word in leftContexts:
	h = 0
	for leftword in leftContexts[word]:
		leftwordProb = 1.0 * leftContexts[word][leftword]/leftwordFreqTotal[word] 
		h += -leftwordProb * math.log(leftwordProb, 2)
	#maxent = math.log(len(set(leftContexts[word].keys())), 2)
	#if maxent > 0.0: entropies[word] = [h/maxent, '--']
	#else: entropies[word] = [h, '--']
	entropies[word] = [h, '--']
for word in rightContexts:
	h = 0
	for rightword in rightContexts[word]:
		rightwordProb = 1.0 * rightContexts[word][rightword]/rightwordFreqTotal[word]
		h += -rightwordProb * math.log(rightwordProb, 2)
	#maxent = math.log(len(set(rightContexts[word].keys())), 2)
#	if word not in entropies:
#		if maxent > 0.0: entropies[word] = ['--', h/maxent]
#		else: entropies[word] = ['--', h]
#	else:
#		if maxent > 0.0: entropies[word][1] = h/maxent
#		else: entropies[word][1] = h
	if word not in entropies:
		entropies[word] = ['--', h]
	else:
		entropies[word][1] = h


for word in entropies:
	print word, '\t', entropies[word][0], '\t', entropies[word][1]
