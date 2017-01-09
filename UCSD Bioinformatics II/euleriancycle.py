from time import time

def EulerianCycle(graph):
	dict = {}
	for line in graph:
		node_index = line.find(' ')
		connect_index = line.find('>')
		node = int(line[:node_index])
		connect_str = line[connect_index+2:]
		connect_list = connect_str.split(',')
		connect_int = map(int,connect_list)
		dict[node] = connect_int
	path = FindCircuit(0,dict)
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

input = open('dataset_203_2.txt','r')
graph = []
for line in input:
	graph.append(line.rstrip())
input.close()

start = time()
output = EulerianCycle(graph)
print time()-start
output_str = "->".join(map(str,output))
output_file = open('eulerian_cycle_output.txt','w')
output_file.write(output_str)
output_file.close()