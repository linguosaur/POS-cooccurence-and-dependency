import math, sys

# returns the number of permutations that have zero matches with correct permutation
# updates fvals if need be; otherwise, looks it up in fvals
def f(x):
	fvalsLen = len(fvals)
	if x >= fvalsLen:
		for i in range(fvalsLen, x+1):
			fvals.append((i-1) * (fvals[i-2] + fvals[i-1]))
	return fvals[x]

fvals = [1,0]

depfile = open(sys.argv[1])
totalDeps = 0
expCorrect = 0.0 # expected number of correct
for line in depfile:
	splitline = line.split()
	sentLen = len(splitline)
	totalDeps += sentLen

	numCombo = math.factorial(sentLen)
	for i in range(1, sentLen+1): # skip i == 0 because numerator will be 0
		expCorrect += 1.0 * i * f(sentLen-i) / numCombo

print 'total number of dependencies:', totalDeps
print 'number of expected correct:', expCorrect
print 'accuracy/precision/recall:', expCorrect/totalDeps
