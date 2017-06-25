#!/usr/bin/env python3

import sklearn.metrics # for testing correctness
import math
import numpy as np

def Jaccard(set1, set2):
	'''
	set1: one clustering solutions
	set2: another clustering solution
	returns: Jaccard similarity index
	'''
	set_length = len(set1)
	set2_parsed = []
	set1_parsed = []
	for i in range(set_length):
		set1_parsed.append(set1[i].split()[1])
		set2_parsed.append(set2[i].split()[1])
	intserction = 0
	for i in range(set_length):
		if set1_parsed[i] == set2_parsed[i]:
			intserction += 1
	return intserction / set_length

def sci_kit_Jaccard(set1, set2):
	'''
	set1: one clustering solutions
	set2: another clustering solution
	returns: Jaccard similarity index by scikit-learn
	'''
	set_length = len(set1)
	set2_parsed = []
	set1_parsed = []
	for i in range(set_length):
		set1_parsed.append(set1[i].split()[1])
		set2_parsed.append(set2[i].split()[1])
	return sklearn.metrics.jaccard_similarity_score(set1, set2)

def NMI(set1, set2):
	'''
	set1: one clustering solutions
	set2: another clustering solution
	returns: NMI
	'''
	set_length = len(set1)
	set2_parsed = []
	set1_parsed = []
	for i in range(set_length):
		set1_parsed.append(int(set1[i].split()[1]))
		set2_parsed.append(int(set2[i].split()[1]))
	set1_parsed = np.array(set1_parsed)
	set2_parsed = np.array(set2_parsed)

	set1_entropy = 0
	for i in np.unique(set1_parsed):
		pi = sum(set1_parsed == i)/set_length
		if (pi != 0):
			set1_entropy += (pi*math.log(pi))
	
	set2_entropy = 0
	for j in np.unique(set2_parsed):
		pj = sum(set2_parsed == j)/set_length
		if (pj != 0):
			set2_entropy += (pj*math.log(pj))
	
	mutual_information = 0
	for i in np.unique(set1_parsed):
		pi = sum(set1_parsed == i)/set_length
		for j in np.unique(set2_parsed):
			pj = sum(set2_parsed == j)/set_length
			pij = sum(np.logical_and(set1_parsed==i,set2_parsed==j))/set_length
			if (pi != 0 and pj != 0 and pij != 0):
				mutual_information += (pij * math.log((pij/(pi*pj))))
	return mutual_information/(math.sqrt(set1_entropy * set2_entropy))

def sci_kit_NMI(set1, set2):
	'''
	set1: one clustering solutions
	set2: another clustering solution
	returns: NMI by scikit-learn
	'''
	set_length = len(set1)
	set2_parsed = []
	set1_parsed = []
	for i in range(set_length):
		set1_parsed.append(int(set1[i].split()[1]))
		set2_parsed.append(int(set2[i].split()[1]))
	return sklearn.metrics.normalized_mutual_info_score(set1_parsed, set2_parsed)

if __name__ == '__main__':

	partitions = open('data/partitions.txt','r')
	ground_truth = []
	for line in partitions:
		ground_truth.append(line.strip().rstrip())
	partitions.close()

	clustering_solutions = []
	for i in range(5):
		solution = open('data/clustering_'+str(i+1)+'.txt','r')
		solution_clustering = []
		for line in solution:
			solution_clustering.append(line.strip().rstrip())
		solution.close()
		clustering_solutions.append(solution_clustering)

	output_file = open('scores.txt','w+')
	for each in clustering_solutions:
		#print(sci_kit_Jaccard(ground_truth, each), " " ,Jaccard(ground_truth, each))
		#print(sci_kit_NMI(ground_truth, each), " " ,NMI(ground_truth, each))
		output_file.write("{:.7f} {:.7f}\n".format(NMI(ground_truth, each), Jaccard(ground_truth,each)))
	output_file.close()
	exit(0)