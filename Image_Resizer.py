import cv2 #pip install opencv-python 

#Used to read or load our image from the given path
img = cv2.imread("Put your image path here", cv2.IMREAD_UNCHANGED)

#Displaying the image given by the user(Original image)
cv2.imshow("Input(Original image given by the user)", img)
 
#Set your width and height here like sizes=(width,height) 
sizes = (900,500)
  
#Resizing our image using opencv's resize() function
resized_image = cv2.resize(img,sizes, interpolation = cv2.INTER_AREA)

#Displaying our image after the resizing process(Resized image)
cv2.imshow("Output(Resized Image)", resized_image)


cv2.waitKey(0)
cv2.destroyAllWindows()

#***************************************Written by jaxxcoder***************************************