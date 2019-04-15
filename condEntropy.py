import codecs, math, sys

def readClark (word2posfilename):
	posdict = {}

	word2posfile = open(word2posfilename, 'r')
	for line in word2posfile:
		splitline = line.rstrip().split(' ')
		word = splitline[0].strip()
		pos = splitline[1]
		posdict[word] = pos
	
	return posdict	

def readBiemann (word2posfilename):
	posdict = {}

	word2posfile = open(word2posfilename, 'r')
	for line in word2posfile:
		splitline = line.rstrip().split('\t')
		pos = splitline[0].strip()
		words = splitline[2].split(', ')
		for word in words:
			posdict[word] = pos
	
	return posdict

def readGoldStd (word2posfilename):
	posdict = {}

	word2posfile = open(word2posfilename, 'r')
	for line in word2posfile:
		splitline = line.rstrip().split('\t')
		word = splitline[0].strip()
		poslist = splitline[1].split(', ')
		posdict[word] = poslist

	print 'gold standard size:', len(posdict.keys())

	return posdict
	

alg_std_posfreqs = {} # maps cluster to dict that maps gold std. tags to frequency counts
alg_posdict = {}
total_clustags = 0
cluster_totals = {}
option = sys.argv[1]
if option == '-b':
	alg_posdict = readBiemann(sys.argv[2])
elif option == '-c':
	alg_posdict = readClark(sys.argv[2])
print 'alg_posdict size:', len(alg_posdict.keys())
std_posdict = readGoldStd(sys.argv[3])
print 'std_posdict size:', len(std_posdict.keys())

evalwords = 0
for word in alg_posdict:
	cluster = alg_posdict[word] # from algorithm
	if word not in std_posdict: continue
	taglist = std_posdict[word] # from gold standard
	evalwords += 1
	for tag in taglist:
		if cluster in alg_std_posfreqs:
			if tag in alg_std_posfreqs[cluster]:
				alg_std_posfreqs[cluster][tag] += 1
			else:
				alg_std_posfreqs[cluster][tag] = 1
			cluster_totals[cluster] += 1
			total_clustags += 1
		else:
			alg_std_posfreqs[cluster] = {tag: 1}
			cluster_totals[cluster] = 1
			total_clustags += 1

cond_entropy = 0.0
for cluster in alg_std_posfreqs:
	for tag in alg_std_posfreqs[cluster]:
		prob_clustag = alg_std_posfreqs[cluster][tag]
		cond_entropy -= 1.0 * prob_clustag / total_clustags * math.log(1.0 * prob_clustag / cluster_totals[cluster], 2)

print 'words evaluated:', evalwords
print 'H(gold standard tag|learned cluster) =', cond_entropy
