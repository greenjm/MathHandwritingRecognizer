# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 21:37:35 2017

@author: georgedr
"""
import cv2
import numpy as np

def boundingBox(img):
    minX = len(img)
    maxX = 0
    minY = len(img[0])
    maxY = 0

    for x in range(len(img)):
        for y in range(len(img[x])):
            if img[x][y] == 1:
                if x < minX:
                    minX = x
                if x > maxX:
                    maxX = x
                if y < minY:
                    minY = y
                if y > maxY:
                    maxY = y
    ret = (minX, minY, maxX, maxY)
    return ret

def rawBoundingBox(symbolArray):
    boxes = []
    for i in range(len(symbolArray)):
        img = symbolArray[i]
        (minX, minY, maxX, maxY) = boundingBox(img)
        boxes.append( [minX, minY, maxX, maxY] )
    return boxes
    
def resizedBoundBox(symbolArray):
    characters = []
    for i in range(len(symbolArray)):
        img = symbolArray[i]
        (minX, minY, maxX, maxY) = boundingBox(img)
        character = img[minY:maxY+1][minX:maxX+1]

        character = character.astype(float)

        characters.append(cv2.resize(character,(45,45)))
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
