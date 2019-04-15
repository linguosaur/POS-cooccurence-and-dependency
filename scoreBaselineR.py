import math, string, sys

# baseline: every word takes the word to the right as head, except the last word, which is the root

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
		if i < sentLen-1:
			nextArg = string.atoi(splitline[i+1].split('-')[1])
			if head == nextArg:
				numCorrect += 1
		else:
			if head == 0:
				numCorrect += 1

print 'total number of dependencies:', totalDeps
print 'number of expected correct:', numCorrect
print 'accuracy/precision/recall:', 1.0*numCorrect/totalDeps
