'''
    This is the main reader.
'''
import cv2
import matplotlib.pyplot as plt
import numpy as np

def recolor(choiceValue, img):
    if choiceValue == "binarize":
        return binarize(img)
    elif choiceValue == "invert":
    	return invert(img)
    elif "recolor" in choiceValue:
    	return preferenceColor(choiceValue, img)

def binarize(img):
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	bin_img = np.where(img>130, 1, 0)
	return bin_img

def invert(img):
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	inv_img = (255-img)
	return inv_img

def preferenceColor(choiceValue, img):
	if "red" in choiceValue:
		img[:, :, 1] = 0.0
		img[:, :, 2] = 0.0
	elif "green" in choiceValue:
		img[:, :, 0] = 0.0
		img[:, :, 2] = 0.0
	else:
		img[:, :, 0] = 0.0
		img[:, :, 1] = 0.0
	return img