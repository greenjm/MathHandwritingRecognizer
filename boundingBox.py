# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 21:37:35 2017

@author: georgedr
"""
import cv2
import numpy as np

def rawBoundingBox(symbolArray):
    boxes = []
    for i in range(len(symbolArray)):
        img = symbolArray[i]
        [x,y,w,h] = cv2.boundingRect(img)
        boxes[i] = [x,y,x+w-1,y+h-1]
    return boxes
    
def resizedBoundBox(symbolArray):
    characters = []
    for i in range(len(symbolArray)):
        print i
        img = symbolArray[i]
        [x,y,w,h] = cv2.boundingRect(img)
        character = img[y:y+h,x:x+w]
        characters[i] = cv2.resize(character,(45,45))
    return characters
        
#a = np.array([[[0,0,0,1,1,1,1,0,0,0,0,0,0],
#               [0,0,1,1,0,0,0,0,1,0,0,0,0],
#               [1,1,1,0,0,0,0,0,0,1,0,0,0],
#               [0,0,0,1,0,0,0,0,0,1,0,0,0],
#               [0,0,0,0,1,1,1,1,1,0,0,0,0]],
#               [[0,0,0,1,1,1,1,0,0,0,0,0,0],
#               [0,0,1,1,0,0,0,0,1,0,0,0,0],
#               [1,1,1,0,0,0,0,0,0,1,0,0,0],
#               [0,0,0,1,0,0,0,0,0,1,0,0,0],
#               [0,0,0,0,1,1,1,1,1,0,0,0,0]],
#               [[0,0,0,1,1,1,1,0,0,0,0,0,0],
#               [0,0,1,1,0,0,0,0,1,0,0,0,0],
#               [1,1,1,0,0,0,0,0,0,1,0,0,0],
#               [0,0,0,1,0,0,0,0,0,1,0,0,0],
#               [0,0,0,0,1,1,1,1,1,0,0,0,0]]])
#resizedBoundBox(a)
