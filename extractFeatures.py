import cv2
import numpy as np

def extractFeatures(self, bwimage):
            
            
    # circularity
    img = bwimage.copy()
    img1, contours, hierarchy = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
            
    B = contours[1]
    C = B[:,0,0]
    l = C.size
    
    
    if abs(B[0,0,0] - B[l-1,0,0]) + abs(B[0,0,1] - B[l-1,0,1]) == 2:
        P8 = math.sqrt(2)
    else:
        P8 = 1   
    for j in range(0,l-1):    
        if abs((B[j+1,0,0] - B[j,0,0])) + abs(B[j+1,0,1] - B[j,0,1]) == 2:
            P8 = P8 + math.sqrt(2)
        else:
            P8 = P8 + 1
    
    n = np.count_nonzero(bwimage)
    
    circularity = P8*P8/n
    
    
    # elongation
    idx = np.nonzero(bwimage);
    c = idx[1]
    r = idx[0]
    meanx = np.mean(c)
    meany = np.mean(r)
    
    
    pows = 2*np.ones(n)
    
    sigxx = np.sum(np.pow((c-meanx),pows)/n
    sigyy = np.sum(np.pow((r-meany),pows)/n
    sigxy = np.sum(np.multiply((r-meany),(c-meanx)))/n
    
    covMat = np.array([[sigxx, sigxy], [sigxy, sigyy]])
    val, vects = np.linalg.eig(covMat);
    
    
    elongation = math.sqrt(np.maximum(val)/np.min(val.ravel()[flatnonzero(val)]));
    
    
    # principal axis
    maxidx = np.argmax(val)
    principalAxisVector = vects[maxidx]
    
    
    return [circularity, elongation, principalAxisVector]

