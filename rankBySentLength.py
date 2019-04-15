import sys

inputFile = open(sys.argv[1])
inputLines = inputFile.readlines()
sentLenTuples = []

for line_i in range(len(inputLines)):
	sentLenTuples.append((line_i, len(inputLines[line_i].split())))

sentLenTuples.sort(lambda a,b: cmp(a[1], b[1]))

for tupe in sentLenTuples:
	sys.stdout.write(inputLines[tupe[0]])
