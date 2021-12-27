import cv2 #pip install opencv-python 

#Used to read or load our image from the given path
image = cv2.imread("Put your image path here")

#Converting our image from BGR to Grayscale using opencv's cvtColor() function
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Displaying our image after conversion from BGR to Grayscale
cv2.imshow('Grayscale', gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

#***************************************Written by jaxxcoder***************************************