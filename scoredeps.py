import sys

evalfile = open(sys.argv[1])
eval = []
for line in evalfile:
	eval.append(line.split())
evalfile.close()

goldstdfile = open(sys.argv[2])
goldstd = []
for line in goldstdfile:
	goldstd.append(line.split())
goldstdfile.close()

if len(eval) != len(goldstd):
	sys.stderr.write('len(eval) != len(goldstd)\n')

totalDepsEvalled = 0
depsCorrect = 0
for line_i in range(len(eval)):
	evalline = eval[line_i]
	goldstdline = goldstd[line_i]
	totalDepsEvalled += len(evalline)
	if len(evalline) != len(goldstdline):
		sys.stderr.write('len(evalline) != len(goldstdline)\n')
		sys.stderr.write('evalline: ' + ' '.join(evalline) + '\n')
		sys.stderr.write('goldstdline: ' + ' '.join(goldstdline) + '\n')
		sys.exit(-1)
	for dep_i in range(len(evalline)):
		splitevaldep = evalline[dep_i].split('-')
		splitgoldstddep = goldstdline[dep_i].split('-')
		evalhead = splitevaldep[0]
		evalarg = splitevaldep[1]
		goldhead = splitgoldstddep[0]
		goldarg = splitgoldstddep[1]
		if evalarg == goldarg:
			if evalhead == goldhead:
				depsCorrect += 1
		else:
			sys.stderr.write('eval file and gold standard file misaligned.\n')
			sys.exit(-1)

print 'total number of dependencies:', totalDepsEvalled
print 'correct dependencies:', depsCorrect
print 'accuracy/precision/recall:', 1.0*depsCorrect/totalDepsEvalled
