
import cv2
import numpy as np

img = cv2.imread("rectangles.jpg")
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# default LSD
LSD = cv2.createLineSegmentDetector(0)
#lines
dlines = LSD.detect(grayImg)
lines = LSD.detect(grayImg)[0]
for i in range(len(lines)):
   for x1,y1,x2,y2 in lines[i]:
     cv2.line(img,(x1,y1),(x2,y2),(255,255,0),3)



cv2.imshow("LSD image", img)
cv2.waitKey(0)
cv2.imwrite("LSD",img)