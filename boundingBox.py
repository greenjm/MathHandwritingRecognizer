# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 21:37:35 2017
@author: georgedr
"""
import cv2
import numpy as np
import math
def boundingBox(img):
    """
    Given an img containing a single component,
    returns the bounding box of the component.
    """
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
    """
    Given an array of single component binary
    masks, returns an array of bounding boxes
    """
    boxes = []
    for i in range(len(symbolArray)):
        img = symbolArray[i]
        (minX, minY, maxX, maxY) = boundingBox(img)
        boxes.append( [minX, minY, maxX, maxY] )
    return boxes
    
def resizedBoundBox(symbolArray):
    """
    Given an array of single component binary
    masks, returns an array of bounding boxes
    that have been resized to 45x45
    """
    characters = []
    for i in range(len(symbolArray)):
        img = np.array(symbolArray[i])
        (minX, minY, maxX, maxY) = boundingBox(img)
        character = img[minX:maxX+1, minY:maxY+1]
        character = character.astype(float)
        w = maxY-minY
        h = maxX-minX
        char = np.zeros(45)
        if h>w:
            fy = 45.0/h
            character = cv2.resize(character,(int(math.floor(fy*w)),45))
            left = np.zeros((45,int(math.floor((45-fy*w)/2))))
            right = np.zeros((45,int(math.ceil((45-fy*w)/2))))
            character = np.hstack((left,character,right))
        elif w>h:
            fx = 45.0/w
            character = cv2.resize(character,(45,int(math.floor(fx*h))))
            top = np.zeros((int(math.floor((45-fx*h)/2)),45))
            bot = np.zeros((int(math.ceil((45-fx*h)/2)),45))
            character = np.vstack((top.astype(int),character.astype(int),bot.astype(int)))


        character = character.astype(float)
        

        characters.append(cv2.resize(character,(45,45)))
    return characters