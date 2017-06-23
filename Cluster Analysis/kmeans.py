#!/usr/bin/env python3

import numpy as np
from random import sample
import scipy.spatial

def kmeans(data, k):
	'''
	data: list of tuples (x,y)
	k: number of clusters to partition
	returns: python list of cluster assignments
	'''
	all_points = np.array(data, dtype=float)
	
	#randomly get centers
	starting_points_indices = sample(list(range(all_points.shape[0])),k)
	centers = all_points[starting_points_indices,:]
	
	cluster_membership = np.zeros((all_points.shape[0],1))
	converged = False
	
	while not converged:
		
		old_clusterings = np.copy(cluster_membership)
		
		#calculate Euclidean distance and assign to closest center/cluster
		for i in range(len(all_points)):
			center_distances = []
			for mean_center in centers:
				center_distances.append(scipy.spatial.distance.euclidean(all_points[i,:], mean_center))
			cluster_membership[i] = center_distances.index(min(center_distances))
		
		if np.array_equal(old_clusterings, cluster_membership):
			converged = True

			#for visualizing the clusters
			# for i in range(k):
			# 	print(all_points[np.where(cluster_membership == i)[0],:])
			# 	print()

			return np.ndarray.tolist(cluster_membership.astype(int)[:,0])

		#calculate new centers from means
		for i in range(k):
			centers[i,:] = np.mean(all_points[np.where(cluster_membership == i)[0],:], axis = 0)

if __name__ == '__main__':

	#obtain data
	data = []
	points = open("places.txt", 'r')
	for line in points:
		data.append(tuple(line.strip().rstrip().split(',')))
	points.close()

	#output groupings
	groupings = kmeans(data,3)
	clustering_output = open("kmeans_res.txt", "w+")
	for i in range(len(data)):
		clustering_output.write("{} {}\n".format(i,groupings[i]))
	clustering_output.close()

	exit(0)