import re, string, sys

# parsing strategy:
# take POS tags of all words in a sentence as input.
# for each tag, rank all other tags in the sentence by frequency of cooccurence in the same sentence, in the training corpus.
# the head is the top-ranking tag.
# the tag whose top-ranking tag has the lowest cooccurence frequency of all top-ranking tags in the sentence is the root

scoreForUnk = 0.1

def fourth(l):
	return l[3]

# read in condprobs
stats = {}
probsfile = open(sys.argv[1])
pos1 = ''
for line in probsfile:
	line = line.rstrip()
	if line == '': continue
	splitline = re.split('\s+', line)
	if splitline[0] != '' and not splitline[0].startswith('total'):
		pos1 = splitline[0]
		stats[pos1] = {}
	elif splitline[0] == '':
		stats[pos1][splitline[1]] = string.atof(splitline[4])
probsfile.close()

posfile = open(sys.argv[2])
for line in posfile:
	depListPerWord = []
	sentDepList = []
	splitposline = line.strip().split(' ')
	minscore = 1.0
	minscorepos = -1
	for i in range(len(splitposline)):
		pos_i = splitposline[i]
		depListPerWord.append([])
		if pos_i == '_': continue
		for j in range(i)+range(i+1,len(splitposline)):
			pos_j = splitposline[j]
			if pos_j == '_': continue
			if pos_i in stats and pos_j in stats[pos_i]:
				depListPerWord[i].append((i, j, pos_j, stats[pos_i][pos_j]))
			else:
				depListPerWord[i].append((i, j, pos_j, scoreForUnk))
		if len(depListPerWord[i]) > 1:
			depListPerWord[i].sort(key=fourth)
			depListPerWord[i].reverse()
			sentDepList.append(depListPerWord[i][0])
			if depListPerWord[i][0][3] < minscore:
				minscorepos = i
				minscore = depListPerWord[i][0][3]
		else: # this word is not '_', but is the only word that isn't
			sentDepList.append((i, -1, '', -1.0))
			minscorepos = i
	finalDeps = []
	for i in range(len(sentDepList)):
		if i != minscorepos:
			finalDeps.append(repr(sentDepList[i][1]+1) + '-' + repr(sentDepList[i][0]+1))
		else:
			finalDeps.append('0-' + repr(sentDepList[i][0]+1))
	print ' '.join(finalDeps)
