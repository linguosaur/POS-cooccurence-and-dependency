import re, string, sys


stats = {}
depsstats = 3*[0.0]
nodepsstats = 3*[0.0]
totalDeps = 0
splitposlines = []

def addpair (key1, key2, dict):
	if key1 in dict:
		if key2 in dict[key1]:
			dict[key1][key2] += 1
		else:
			dict[key1][key2] = 1
	else:
		dict[key1] = {key2: 1}

depfile = open(sys.argv[1], 'r')
posfile = open(sys.argv[2], 'r')
probsfile = open(sys.argv[3], 'r')
poslines = posfile.readlines()

for line in poslines:
	splitposlines.append(line.split())
posfile.close()

pos1 = ''
for line in probsfile:
	splitline = re.split('\s+', line)
	if line.strip() == '': continue
	if splitline[0] != '' and splitline[0] != 'total:' and splitline[0] != 'total':
		pos1 = splitline[0]
		stats[pos1] = {}
	elif splitline[0] == '':
		stats[pos1][splitline[1]] = map(string.atof, splitline[2:5])
	elif splitline[0] == 'total': totalPairs = string.atoi(splitline[2])
probsfile.close()

setOfAll = set()
for pos1 in stats:
	for pos2 in stats[pos1]:
		setOfAll.add(pos1+' '+pos2)

setOfDeps = set()
deps = {}
depfilelines = depfile.readlines()
for line_i in range(len(depfilelines)):
	splitdepline = depfilelines[line_i].split()
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
depfile.close()

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
nodeps = {}
for pospair in setOfNoDeps:
	splitpospair = pospair.split()
	head = splitpospair[0]
	arg = splitpospair[1]
	nodepsstats[0] += stats[head][arg][1]
	nodepsstats[1] += stats[head][arg][2]
	nodepsstats[2] += stats[arg][head][2]
	totalNoDepPairs += 1
	addpair(head, arg, nodeps)
for i in range(len(nodepsstats)):
	nodepsstats[i] /= totalNoDepPairs

for head in deps:
	for arg in deps[head]:
		deps[head][arg] /= 1.0 * stats[head][arg][0]

print 'deps'
print
for head in deps:
	print head, ':'
	keys = deps[head].keys()
	keys.sort(key=deps[head].get)
	keys.reverse()
	for arg in keys:
		print '\t', arg, '\t', deps[head][arg], '\t', stats[head][arg][0], '\t', stats[head][arg][1], '\t', stats[head][arg][2], '\t', stats[arg][head][2]
print
print 'nodeps'
print
for head in nodeps:
	print head, ':'
	keys = nodeps[head].keys()
	keys.sort(key=nodeps[head].get)
	keys.reverse()
	for arg in keys:
		print '\t', arg, '\t', '--', '\t', stats[head][arg][0], '\t', stats[head][arg][1], '\t', stats[head][arg][2], '\t', stats[arg][head][2]

print 'dependencies:', depsstats
print 'non-dependencies:', nodepsstats
