#!/usr/bin/env python3

import cv2
import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("error")

def auto_canny(img, sigma=0.33):
	median = np.median(img)
	lower = int(max(0,(1-sigma)*median))
	upper = int(min(255,(1+sigma)*median))
	edged = cv2.Canny(img,lower,upper, L2gradient = True)
	return edged

imgs = ["test.tif", "test2.tif", "test3.tif"]

for tif in imgs:

	img = cv2.imread(tif, cv2.IMREAD_GRAYSCALE)
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

	# cv2.imshow('image',edges)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

	img2, cnts, hier = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

	curvatures = []

	for each in cnts:
		for i in range(each.shape[0]):

			pos = each[i,0]

			if i == 0:
				posOld = pos
				posOlder = pos

			x_deriv1 = pos[0] - posOld[0]
			x_deriv2 = -pos[0] + 2*posOld[0] - posOlder[0]
			y_deriv1 = pos[1] - posOld[1]
			y_deriv2 = -pos[1] + 2*posOld[1] - posOlder[1]

			curvature = 0
			if (abs(x_deriv2) > float(10e-4) and abs(y_deriv2) > float(10e-4)):
				try:
					top=pow(y_deriv2*x_deriv1 - x_deriv2*y_deriv1,2)
					bottom=pow(x_deriv2 + y_deriv2,3)
					if bottom < 0:
						continue
					elif bottom == 0:
						curvature = 99
					else:
						curvature = np.sqrt(top/bottom)
					if curvature == float("Inf"):
						curvature = 99
				except RuntimeWarning:
					print("RuntimeWarning")
					print(top)
					print("----")
					print(bottom)

					#print("RunetimeWarning")
					#print(top)
					#print("----")
					#print(bottom)
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
	print("Low: {}".format(low))
	print("High: {}".format(high))
	print("High/Low: {}".format(high/low))
	print("Average: {}".format(np.mean(curvatures)))


	#cv2.drawContours(color_img,cnts[1],-1,(0,0,255),1)

	#print(cnts[1][1])

	#epsilon = 0.1 * cv2.arcLength(cnts[1][1],False)
	#approx = cv2.approxPolyDP(cnts[1][1],epsilon,True)

	#cnts[1][1] = approx

	# cv2.drawContours(color_img,cnts,-1,(0,0,255),1)

	# cv2.imshow('image',color_img)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

	#edges = cv2.Canny(img, 75, 150, apertureSize=3, L2gradient = True)
	# #print(edges)

	# lines = cv2.HoughLines(edges,8,np.pi/180,360)

	# for each in lines:
	# 	for rho,theta in each:
	# 		a = np.cos(theta)
	# 		b = np.sin(theta)
	# 		x0 = a*rho
	# 		y0 = b*rho
	# 		x1 = int(x0 + 1000*(-b))
	# 		y1 = int(y0 + 1000*a)
	# 		x2 = int(x0 - 1000*(-b))
	# 		y2 = int(y0 - 1000*a)
	# 		cv2.line(img, (x1,y1),(x2,y2),(255,0,0),2)

	# cv2.imwrite("houghlines3.jpg",img)

	#cv2.imshow('image',edges)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
