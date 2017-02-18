# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 14:17:59 2017

@author: georgedr
"""
import cv2
import numpy as np

def extractHOG(image):
    """
    Given an image of size 45x45, returns a HOG feature vector
    """
    image = deskew(image)
    winSize = (45,45)
    blockSize = (21,21)
    blockStride = (8,8)
    cellSize = (7,7)
    nbins = 9
    derivAperture = 1
    winSigma = 4.
    histogramNormType = 0
    L2HysThreshold = 2.0000000000000001e-01
    gammaCorrection = 0
    nlevels = 64
    hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins,derivAperture,winSigma,histogramNormType,L2HysThreshold,gammaCorrection,nlevels)
    return hog.compute(image)
    
    
def deskew(img):
    m = cv2.moments(img)
    if abs(m['mu02']) < 1e-2:
        # no deskewing needed. 
        return img.copy()
    # Calculate skew based on central momemts. 
    skew = m['mu11']/m['mu02']
    # Calculate affine transform to correct skewness. 
    M = np.float32([[1, skew, -0.5*45*skew], [0, 1, 0]])
    # Apply affine transform
    img = cv2.warpAffine(img, M, (45, 45), flags=cv2.WARP_INVERSE_MAP | cv2.INTER_LINEAR)
    return img