import math, sys

# calculate Euclidean distance between two word context distributions (halfwords)
def simScore(word1, word2):
	simScore = 0.0
	word1Norm = 0.0
	word2Norm = 0.0
	for contextword in word1:
		if contextword in word2:
			simScore += 1.0 * word1[contextword] * word2[contextword]
			word1Norm += word1[contextword] * word1[contextword]
			word2Norm += word2[contextword] * word2[contextword]
	if simScore > 0.0: simScore /= 1.0 * word1Norm * word2Norm
	return simScore

leftContexts = {}
rightContexts = {}
n = 10

print >> sys.stderr, 'gathered contexts . . . ',
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
				else:
					leftContexts[thisword] = {leftword: 1}
			if i < len(splitline)-1:
				rightword = splitline[i+1]
				if thisword in rightContexts:
					if rightword in rightContexts[thisword]:
						rightContexts[thisword][rightword] += 1
					else:
						rightContexts[thisword][rightword] = 1
				else:
					rightContexts[thisword] = {rightword: 1}

print >> sys.stderr, 'done'
print >> sys.stderr, 'calculating simscores . . . '

leftSimScores = {}
rightSimScores = {}
#words = leftContexts.keys()
words = ['ang', 'tao', 'maganda', 'kumain', 'kinain', 'umawit', 'pinatay', 'anak', 'kotse', 'ng', 'sa', 'para', 'tungkol', 'siya', 'sila', 'niya', 'nila', 'lalake', 'babae', 'libro']
print >> sys.stderr, 'left:'
for i in range(len(words)):
	for j in range(i+1, len(words)):
		leftSimScores[words[i]+' '+words[j]] = simScore(leftContexts[words[i]], leftContexts[words[j]])
#words = rightContexts.keys()
print >> sys.stderr, 'right:'
for i in range(len(words)):
	for j in range(i+1, len(words)):
		rightSimScores[words[i]+' '+words[j]] = simScore(rightContexts[words[i]], rightContexts[words[j]])

print >> sys.stderr, 'done'
print >> sys.stderr, 'sorting . . . '
		
leftKeys = leftSimScores.keys()
leftKeys.sort(key=leftSimScores.get)
leftKeys.reverse()
rightKeys = rightSimScores.keys()
rightKeys.sort(key=rightSimScores.get)
rightKeys.reverse()
print 'left context similarities:'
for k in leftKeys:
	print k, '\t', leftSimScores[k]
print
print 'right context similarities:'
for k in rightKeys:
	print k, '\t', rightSimScores[k]
