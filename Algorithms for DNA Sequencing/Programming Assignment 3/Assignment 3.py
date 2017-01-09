__author__ = 'Alec'

# parses a DNA reference genome from a file in FASTA format
def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

def editDistance(x, y):
    # Create distance matrix
    D = []
    for i in range(len(x)+1):
        D.append([0]*(len(y)+1))

    # Initialize first row and column of matrix
    for i in range(len(x)+1):
        D[i][0] = i
    for i in range(len(y)+1):
        D[0][i] = 0

    # Fill in the rest of the matrix
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            distHor = D[i][j-1] + 1
            distVer = D[i-1][j] + 1
            if x[i-1] == y[j-1]:
                distDiag = D[i-1][j-1]
            else:
                distDiag = D[i-1][j-1] + 1

            D[i][j] = min(distHor, distVer, distDiag)

    # Edit distance is the value in the bottom right corner of the matrix
    #return D[-1][-1]
    minim = D[-1][-1]
    for i in range (1,len(y)+1):
        if D[-1][i] < minim:
            minim = D[-1][i]
    return minim

def overlap(a, b, min_length=3):
    """ Return length of longest suffix of 'a' matching
        a prefix of 'b' that is at least 'min_length'
        characters long.  If no such overlap exists,
        return 0. """
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's suffx in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match

# parses the read and quality string from a FASTQ file
def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()
            seq = fh.readline().rstrip()
            fh.readline()
            qual = fh.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities

genome = readGenome("chr1.GRCh38.excerpt.fasta")

print editDistance("GCTGATCGATCGTACG",genome)
print
print editDistance("GATTTACCAGATTGAG",genome)
print

genome2, _ = readFastq("ERR266411_1.for_asm.fastq")
kmer_set = {}
for read in genome2:
    for j in range(len(read)-30+1):
        if read[j:j+30] not in kmer_set:
            kmer_set[read[j:j+30]] = set()
            kmer_set[read[j:j+30]].add(read)
        else:
            kmer_set[read[j:j+30]].add(read)

final = []
for read in genome2:
    for o in kmer_set[read[-30:]]:
        if overlap(read, o, 30) > 0:
            if read != o:
                final.append(read)

print len(final)
print
blue = set()
for read in genome2:
    for o in kmer_set[read[-30:]]:
        if overlap(read, o, 30) > 0:
            if read != o:
                blue.add(read)

print len(blue)