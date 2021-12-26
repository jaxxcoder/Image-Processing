import cv2 #pip install opencv-python

#Used to read or load our image from the given path
image = cv2.imread("Put your image path here")

#Converting our image from BGR to RGB using opencv's cvtColor() function
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#Displaying our image after conversion from BGR to RGB
cv2.imshow('image', image_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()

#***************************************Written by jaxxcoder***************************************
