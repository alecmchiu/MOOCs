from itertools import product
from collections import defaultdict
#from sys import setrecursionlimit

def DeBruijn3(patterns):
	graph = []
	dict = defaultdict(list)
	for each in patterns:
		dict[each[:-1]].append(each[1:])
	for each in sorted(dict):
		string = each + ' -> '
		for item in dict[each]:
			string = string + item + ','
		graph.append(string[:-1])
	return graph

def EulerianCycle(graph):
	dict = {}
	for line in graph:
		node_index = line.find(' ')
		connect_index = line.find('>')
		node = line[:node_index]
		connect_str = line[connect_index+2:]
		connect_list = connect_str.split(',')
		dict[node] = connect_list
	path = FindCircuit(dict.keys()[0],dict)
	return path[::-1]
			
def FindCircuit(node,dict):
	dict_copy = dict.copy()
	final_path = []
	if (len(dict_copy[node]) == 0):
		final_path.append(node)
		return final_path
	else:
		while (len(dict_copy[node]) != 0):
			next = dict_copy[node].pop()
			final_path += FindCircuit(next,dict_copy)
		final_path.append(node)
	return final_path

def combine(ls):
	combined = ls[0]
	for i in range(1,len(ls)):
		combined = combined + ls[i][-1]
	return combined	

#setrecursionlimit(5000)

def kunverisal(k):
	kmers = [''.join(x) for x in product('01',repeat=k)]
	return kmers

string = combine(EulerianCycle(DeBruijn3(kunverisal(4))))
print len(string)
print len('0000110010111101')
output = open("kunverisal.txt",'w')
output.write(string)
output.close()