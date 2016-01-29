def readfasta (fasta):
    input = open(fasta, 'r')
    seqs = {}
    for line in input:
        if line[0] == '>':
            name = line[1:].rstrip()
            seqs[name] = [] 
        else:
            seqs[name].append(line.rstrip())
    for name in seqs:
        seqs[name] = ''.join(seqs[name])
    input.close
    return seqs

seqs = readfasta('test.txt')

str1 = seqs['Rosalind_7466']
str2 = seqs['Rosalind_3417']
def findnt(nt, string, first):
	for n in range (first, len(str1)):
		if nt == str1[n]: 
			return (n)

result = []
n = 0
for nt in str2:
	first = n
	n = findnt(nt, str1, first)
	result.append(n+1)
	
for n in result:
	print n,