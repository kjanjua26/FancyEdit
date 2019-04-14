'''
    This is the main reader.
'''
import cv2
import matplotlib.pyplot as plt
import numpy as np

def recolor(choiceValue, img):
    if choiceValue == "binarize":
        return binarize(img)

def binarize(img):
    bin_img = np.where(img>130, 1, 0)
    return bin_img