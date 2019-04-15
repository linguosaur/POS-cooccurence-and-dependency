import re, string, sys

stats = {}
depsstats = 3*[0.0] # [<cooccurence>, <P(head|arg)>, <P(arg|head)>]
nodepsstats = 3*[0.0] # same 
totalDeps = 0
splitposlines = []

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
		stats[pos1][splitline[1]] = map(string.atof, splitline[3:5])
	elif splitline[0] == 'total': totalPairs = string.atoi(splitline[2])
probsfile.close()

depfilelines = depfile.readlines()
for line_i in range(len(depfilelines)):
	splitdepline = depfilelines[line_i].split()
	splitposline = splitposlines[line_i]
	totalDeps += len(splitdepline)
	for i in range(len(splitposline)-1):
		for j in range(i+1, len(splitposline)):
			posi = splitposline[i]
			posj = splitposline[j]
			# in deps file, dependencies are of form <head>-<arg>
			if repr(i+1)+'-'+repr(j+1) in splitdepline:
				depsstats[0] += stats[posi][posj][0]
				depsstats[1] += stats[posi][posj][1]
				depsstats[2] += stats[posj][posi][1]
			elif repr(j+1)+'-'+repr(i+1) in splitdepline:
				depsstats[0] += stats[posj][posi][0]
				depsstats[1] += stats[posj][posi][1]
				depsstats[2] += stats[posi][posj][1]
			else:
				nodepsstats[0] += stats[posi][posj][0]
				nodepsstats[1] += stats[posi][posj][1]
				nodepsstats[2] += stats[posj][posi][1] # nodepsstats[1] and nodepsstats[2] meant to be averaged later
depfile.close()

for i in range(len(depsstats)):
	depsstats[i] /= totalDeps
for i in range(len(nodepsstats)):
	nodepsstats[i] /= (totalPairs - totalDeps)
nodepsstats[1] = (nodepsstats[1] + nodepsstats[2]) / 2.0
nodepsstats[2] = nodepsstats[1]

print 'dependencies: ', depsstats
print 'non-dependencies: ', nodepsstats
