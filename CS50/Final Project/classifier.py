#!/usr/bin/env python3

import cv2
import numpy as np
import matplotlib.pyplot as plt
import warnings
import sys
import os

warnings.filterwarnings("error")

def auto_canny(img, sigma=0.33):
	median = np.median(img)
	lower = int(max(0,(1-sigma)*median))
	upper = int(min(255,(1+sigma)*median))
	edged = cv2.Canny(img,lower,upper, L2gradient = True)
	return edged

if __name__ == '__main__':

	if len(sys.argv) != 2:
		print("Usage: python classifier.py directory",file=sys.stderr)
		exit(1)
	else:
		all_files = os.listdir(sys.argv[1])
		imgs = []
		for each in all_files:
			if each.endswith(".tif"):
				imgs.append(each)
		directory = sys.argv[1]

	#imgs = ["test.tif", "test2.tif", "test3.tif"]

	ratios = []
	averages = []

	for tif in imgs:

		img = cv2.imread(directory+"/"+tif, cv2.IMREAD_GRAYSCALE)
		#thresh = cv2.threshold(img, 100,255,cv2.THRESH_BINARY_INV)[1]

		blurred = cv2.GaussianBlur(img, (5,5), 0)
		thresh = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,33,2)
		denoised = cv2.fastNlMeansDenoising(thresh, None, 75, 45, 20)

		#cnts = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		#cv2.drawContours(img,cnts[1],-1,(255,255,255),3)

		#cv2.imshow('image',denoised)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()

		edges = auto_canny(denoised, 0.33)

		#cv2.imshow('image',edges)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()

		#blurred_edges = cv2.GaussianBlur(edges, (3,3), 0)
		#thresh_edges = cv2.threshold(blurred_edges,25,255,cv2.THRESH_BINARY)[1]
		#edges2 = auto_canny(thresh_edges, 0.33)

		#cv2.imshow('image',edges2)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()

		img2, cnts, hier = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

		#color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

		#cv2.drawContours(color_img,cnts,-1,(0,0,255),1)

		#cv2.imshow('image',color_img)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()

		curvatures = []

		for each in cnts:
			for i in range(each.shape[0]):

				pos = each[i,0]

				if i == 0:
					posOld = pos
					posOlder = pos

				x_deriv1 = pos[0] - posOld[0]
				x_deriv2 = -pos[0] + 2.0*posOld[0] - posOlder[0]
				y_deriv1 = pos[1] - posOld[1]
				y_deriv2 = -pos[1] + 2.0*posOld[1] - posOlder[1]

				curvature = 0
				if (abs(x_deriv2) > float(10e-4) and abs(y_deriv2) > float(10e-4)):
					try:
						top=pow(y_deriv2*x_deriv1 - x_deriv2*y_deriv1,2)
						bottom=pow(x_deriv2 + y_deriv2,3)
						if bottom == 0:
							curvature = 0
						else:
							curvature = np.sqrt(abs(top/bottom))
					except RuntimeWarning:
						print("RuntimeWarning")
						print(top)
						print("----")
						print(bottom)

				curvatures.append(curvature)

				posOlder = posOld
				posOld = pos

		low = 0
		high = 0

		for each in curvatures:
			if each > 0.5:
				high +=1
			else:
				low +=1
		#print("Low: {}".format(low))
		#print("High: {}".format(high))
		#print("High/Low: {}".format(high/low))
		#print("Average: {}".format(np.mean(curvatures)))
		#print("---------------")
		ratios.append(high/low)
		averages.append(np.mean(curvatures))

# for each in ratios:
# 	print(each)
# print("----")
# for each in averages:
# 	print(each)
print("------")
print("Average ratio: {}".format(np.mean(ratios)))
print("Average curvature: {}".format(np.mean(averages)))
exit(0)


		#cv2.drawContours(color_img,cnts[1],-1,(0,0,255),1)

		#print(cnts[1][1])

		#epsilon = 0.1 * cv2.arcLength(cnts[1][1],False)
		#approx = cv2.approxPolyDP(cnts[1][1],epsilon,True)

		#cnts[1][1] = approx

		# cv2.drawContours(color_img,cnts,-1,(0,0,255),1)

		# cv2.imshow('image',color_img)
		# cv2.waitKey(0)
		# cv2.destroyAllWindows()

		#cv2.imshow('image',edges)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()
