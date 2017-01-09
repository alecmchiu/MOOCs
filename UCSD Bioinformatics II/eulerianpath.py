from time import time

def EulerianPath(graph):
	dict = {}
	indegree_dict = {}
	bad_indegree = 0
	bad_outdegree = 0
	bad_in_degree_bool = False
	
	for line in graph:
		node_index = line.find(' ')
		connect_index = line.find('>')
		node = int(line[:node_index])
		connect_str = line[connect_index+2:]
		connect_list = connect_str.split(',')
		connect_int = map(int,connect_list)
		dict[node] = connect_int

	non_values = []

	for key in dict.keys():
		for value in dict[key]:
			if value not in dict.keys():
				non_values.append(value)

	for item in non_values:
		dict[item] = []
		bad_outdegree = item

	for key in dict:
		indegree_dict[key] = 0

	for key in dict:
		for value in dict[key]:
			indegree_dict[value] += 1

	for key in dict:
		if (len(dict[key]) != indegree_dict[key]):
			if key != bad_outdegree:
				bad_indegree = key
				bad_in_degree_bool = True

	if (len(non_values)!=0):
		dict[bad_outdegree].append(bad_indegree)

	path = FindCircuit(bad_indegree,dict)

	if (len(non_values) != 0):
		path = path[1:]

	path = path[::-1]
	
	if (not bad_in_degree_bool):
		brk = path.index(bad_outdegree)
		part1 = path[brk:]
		part2 = path[:brk]
		path = part1 + part2
	
	return path
			
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

input = open('dataset_203_5.txt','r')
graph = []
for line in input:
	graph.append(line.rstrip())
input.close()

start = time()
output = EulerianPath(graph)
print time()-start,'seconds'
output_str = "->".join(map(str,output))
output_file = open('eulerian_path_output.txt','w')
output_file.write(output_str)
output_file.close()