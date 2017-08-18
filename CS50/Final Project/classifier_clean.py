#!/usr/bin/env python3

import cv2
import numpy as np
import sys
import os

def auto_canny(img, sigma=0.33):
	'''
	img: image as read in by OpenCV
	sigma: pertubation parameter
	return: returns image of Canny detected edges
	Automatically decides parameters for canny edge detection using Euclidean distance
	'''
	median = np.median(img)
	lower = int(max(0,(1-sigma)*median))
	upper = int(min(255,(1+sigma)*median))
	edged = cv2.Canny(img,lower,upper, L2gradient = True)
	return edged

def getCurvature(contour, step):
	'''
	contour: set of points for a contour
	step: step size between points of a contour
	Calculates curvature for the supplied contour using an approximation of
		the curvature equation from calculus
	'''
	vecCurvature = [0] * len(contour)
	if len(contour) < step:
		return vecCurvature

	frontToBack = contour[0] - contour[-1]
	isClosed = max(abs(frontToBack[0]),abs(frontToBack[1])) <= 1

	for i in range(len(contour)):
		pos = contour[i]
		maxStep = step
		if (not isClosed):
			maxStep = min(min(step,i),len(contour)-1-i)
			if (maxStep == 0):
				vecCurvature[i] = sys.maxsize
		iminus = i - maxStep
		iplus = i + maxStep
		pminus = contour[iminus + len(contour)-1 if iminus < 0 else iminus]
		pplus = contour[iplus-len(contour)-1 if iplus > len(contour)-1 else iplus]

		if (iplus-iminus) == 0:
			vecCurvature[i] = sys.maxsize
			continue
		f1stDeriv_x = (pplus[0] - pminus[0])/(iplus-iminus)
		f1stDeriv_y = (pplus[1] - pminus[1])/(iplus-iminus)
		f2ndDeriv_x = (pplus[0] - 2*pos[0] + pminus[0])/((iplus-iminus)/2*(iplus-iminus)/2)
		f2ndDeriv_y = (pplus[1] - 2*pos[1] + pminus[1])/((iplus-iminus)/2*(iplus-iminus)/2)

		curvature2D = 0
		divisor = f1stDeriv_x*f1stDeriv_x + f1stDeriv_y*f1stDeriv_y
		if (abs(divisor) > float(10e-8)):
			curvature2D = abs(abs(f2ndDeriv_y*f1stDeriv_x - f2ndDeriv_x*f1stDeriv_y)/pow(divisor,3.0/2.0))
		else:
			curvature2D = sys.maxsize
		vecCurvature[i] = curvature2D
	return vecCurvature

if __name__ == '__main__':

	if len(sys.argv) != 3:
		print("Usage: python classifier.py directory output_file",file=sys.stderr)
		exit(1)
	else:
		all_files = os.listdir(sys.argv[1])
		imgs = []
		for each in all_files:
			if each.endswith(".tif"):
				imgs.append(each)
		directory = sys.argv[1]

	averages = []

	for tif in imgs:

		#read in image as grayscale
		img = cv2.imread(directory+"/"+tif, cv2.IMREAD_GRAYSCALE)

		#apply gaussian blur to exaggerate edges
		blurred = cv2.GaussianBlur(img, (5,5), 0)

		#apply adaptive gaussian threshold and binarize picture
		thresh = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,33,2)
		
		#denoise to remove small artifacts
		denoised = cv2.fastNlMeansDenoising(thresh, None, 75, 45, 20)

		#apply canny edge detection from processed image
		edges = auto_canny(denoised, 0.33)

		#convert edges to contours
		img2, cnts, hier = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

		all_curv = []
		high_curv = 0

		#record curvature for all contours
		for each in cnts:
			all_curv.extend(getCurvature(each[:,0,:],1))

		#count number of high curvature points
		for each in all_curv:
			if each >= 1:
				high_curv += 1
		averages.append(high_curv)

#classify as live or dead based on number of high curvature points
output_file = open(sys.argv[2], "w+")
for each in averages:
	dist_live = abs(111.5 - each)
	dist_dead = abs(97.5 - each)
	status = "Live" if dist_live < dist_dead else "Dead"
	output_file.write(status + "\n")
output_file.close()
exit(0)
