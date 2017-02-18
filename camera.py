import cv2


vc = cv2.VideoCapture(1)
i = 0
if vc.isOpened():

	while True:
		rval, frame = vc.read()
		cv2.imshow("feed me a problem", frame)
		key = cv2.waitKey(20)
		if key == 27: 
			cv2.destroyWindow("feed me a problem")
			vc.release()
			break
		elif key == ord('p'):
			i+=1
			filename = "C:/Users/georgedr/Documents/GitHub/MathHandwritingRecognizer/testimg"+str(i)+".png"
			cv2.imwrite(filename,frame)



