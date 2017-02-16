import sys
import cv2
import numpy as np
import segmentation as seg
import connectedComponents as cc
import boundingBox as bb
import extractHOG as hog
import svm
import symbolDict as d

def main():
	#Load Image
	imgPath = sys.argv[1]
	img = cv2.imread(imgPath, 0)
	display = raw_input("Image loaded. Display? (y/n): ")
	if display=="y":
		cv2.startWindowThread()
		cv2.imshow("Original", img)
		cv2.waitKey(1)

	#Segment Image
	segmented = seg.segmentImage(img)
	display = raw_input("Image has been segmented. Display? (y/n): ")
	if display=="y":
		cv2.startWindowThread()
		cv2.imshow('Segmented', segmented)
		cv2.waitKey(1)

	#Connected Components
	print "Gathering connected components..."
	conn = cc.connectedComponents(segmented)
	components = conn.findConnectedComponents()
	symbols = conn.createComponentMasks()
	raw_input("Found connected components. Press any button to continue.")

	#Bounding Boxes (raw and resized)
	print "\nGathering bounding boxes..."
	bboxes = bb.rawBoundingBox(symbols)
	print "\nResizing for classification..."
	resized = bb.resizedBoundBox(symbols)

	#Extract HOG
	print "\nExtracting HOG features for all components..."
	features = []
	for i in range(0, len(resized)):
		features.append(np.hstack(
			np.array(
				hog.extractHOG(
					np.uint8(resized[i])#.astype(np.uint8)
				)
			)
		))
	raw_input("All features extracted. Press any button to begin classifying")

	#SVM Classification
	syms = d.getDict()
	print "\nSending features for classification by voting..."
	preds = svm.voteClassify(features, 5, 5)
	display = raw_input("Raw classification complete. Display? (y/n): ")
	if display=="y":
		print "\n--------------- RAW CLASSIFICATIONS ---------------"
		for i in range(0, len(preds)):
			print "Component:", i+1, "Classification:", syms[preds[i]]
		print "-------------------- DONE --------------------"

	doGrammar = raw_input("Classification done. Proceed with grammar? (y/n)")
	if doGrammar=="y":
		print "TODO"
		#XY-cut
		#Symbol combination

	#Program Ended
	raw_input("End of program. Press any button to quit.")

if __name__=="__main__":
	main()