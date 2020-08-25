import cv2
import numpy as np


img = cv2.imread('rectangles.jpg')
#blur a little bit
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
image = cv2.medianBlur(img,3)
#canny and detect lines using it
canny = cv2.Canny(img,150,150,2)
lines = cv2.HoughLinesP(canny,1,np.pi/180,10,0,0)

#draw lines
for i in range(len(lines)):
   for x1,y1,x2,y2 in lines[i]:
     cv2.line(img,(x1,y1),(x2,y2),(255,255,0),3)

cv2.imshow('rects',img)
cv2.waitKey(0)
cv2.imwrite('houghlines5.jpg',img)