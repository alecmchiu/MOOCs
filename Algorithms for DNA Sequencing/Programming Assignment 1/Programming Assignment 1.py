__author__ = 'Alec'

"""
Programming Assignment Goals:
1. Implement strand awareness for naive exact matching algorithm
2. If the string is a palindrome, naive exact matching algorithm returns same results as original function
3. Perform test cases for strand awareness naive exact matching algorithm
4. Create a naive exact matching algorithm that allows for up to 2 mismatches
5. Perform test cases for 2 mismatch naive exact matching algorithm
6. Search for bad sequencing spot for FASTQ file

"""

# Given Functions:

# return reverse complement of string
def reverseComplement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N':'N'}
    t =''
    for base in s:
        t = complement[base] + t
    return t

# naive exact matching algorithm

# original naive exact matching algorithm
def naive(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if t[i+j] != p[j]:
                match = False
                break
        if match:
            occurrences.append(i)
    return occurrences

# naive exact algorithm with strand awareness
def naive_with_rc(p, t):
    occurrences = []
    rp = reverseComplement(p)
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if t[i+j] != p[j]:
                match = False
                break
        if match:
            occurrences.append(i)
    if p != rp:
        for i in range(len(t) - len(rp) + 1):
            match = True
            for j in range(len(rp)):
                if t[i+j] != rp[j]:
                    match = False
                    break
            if match:
                occurrences.append(i)
    return occurrences

# naive exact algorithm with up to 2 mm

def naive_2mm(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        mm = 0
        for j in range(len(p)):
            if t[i+j] != p[j]:
                mm += 1
        if mm <= 2:
            occurrences.append(i)
    return occurrences

# parses a DNA reference genome from a file in FASTA format
def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

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

#######

# New functions:

def phred33toq(qual):
    return ord(qual) - 33

def most_common(lst):
    return max(set(lst), key = lst.count)

######

# Exercise Outputs

genome = readGenome("/Users/Alec/IdeaProjects/Coursera - Algorithms for DNA Sequencing - Programming Assignments/Programming Assignment 1/lambda_virus.fa")

# reverse compliment exercises
print "AGGT or its reverse complement appears %d times" % len(naive_with_rc("AGGT",genome))
print "TTAA or its reverse complement appears %d times" % len(naive_with_rc("TTAA",genome))
print "The leftmost occurrence of ACTAAGT or its reverse compliment is at index: %d" % min(naive_with_rc("ACTAAGT",genome))
print "The leftmost occurrence of AGTCGA or its reverse compliment is at index: %d" % min(naive_with_rc("AGTCGA",genome))

# 2mm exercises
print "TTCAAGCC appears %d times when allowing for up to two mismatches" % len(naive_2mm("TTCAAGCC",genome))
print "The leftmost occurrence of AGGAGGTT or its reverse compliment is at index: %d" % min(naive_2mm("AGGAGGTT",genome))

# error searching exercises
_, phred_quality = readFastq("/Users/Alec/IdeaProjects/Coursera - Algorithms for DNA Sequencing - Programming Assignments/Programming Assignment 1/ERR037900_1.first1000.fastq") #ignore base sequence
true_quality = []

for line in phred_quality:
    new =[]
    for qual in line:
        new.append(phred33toq(qual))
    true_quality.append(new)

lowest_indicies = []
for line in true_quality:
    lowest_indicies.append(line.index(min(line)))

print "The faulty sequence site is %d" % most_common(lowest_indicies)