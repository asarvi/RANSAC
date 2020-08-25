import cv2
import numpy as np
#read image and turn it to gray
image = cv2.imread('Balls.jpg',0)
imageGray = cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)
#blur the pic a little to be smoother
image = cv2.medianBlur(image,5)
#find hough circles
Hcircles = cv2.HoughCircles(image,cv2.HOUGH_GRADIENT,1,200, param1=50,param2=50,minRadius=0,maxRadius=0)
for x in Hcircles[0,:]:
    cv2.circle(imageGray,(x[0],x[1]),x[2],(250,255,0),5)

cv2.imshow('circles',imageGray)
cv2.waitKey(0)