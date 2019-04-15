import math, string, sys

# baseline: every word takes the word to the left as head, except the first word, which is the root

depfile = open(sys.argv[1])
totalDeps = 0
numCorrect = 0
for line in depfile:
	splitline = line.split()
	sentLen = len(splitline)
	totalDeps += sentLen

	for i in range(sentLen):
		splitDep = splitline[i].split('-')
		head = string.atoi(splitDep[0])
		if i == 0:
			if head == 0:
				numCorrect += 1
		else:
			lastArg = string.atoi(splitline[i-1].split('-')[1])
			if head == lastArg:
				numCorrect += 1

print 'total number of dependencies:', totalDeps
print 'number of expected correct:', numCorrect
print 'accuracy/precision/recall:', 1.0*numCorrect/totalDeps
