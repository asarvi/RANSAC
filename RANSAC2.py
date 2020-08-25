import cv2
import numpy as np
import math
import statistics

img = cv2.imread('line2.bmp')

height = img.shape[0]
width = img.shape[1]

whitesx = []
whitesy = []
#for choosen white pixels
whitesxx =[]
whitesyy= []

def Ransac():
    distances = []
    #repeat the algorithm 5 times
    for l in range(5):
        # put white positions in whites
        for i in range(width):
            for j in range(width):
                if (img[i, j][1] > 0):
                    whitesxx.append(i)
                    whitesyy.append(j)

        print(len(whitesyy))
         #chose 30 numbers from 56 white pixels
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,
                   51,52,53,54,55]
        # choose 30 of random whites
        randomMembers = np.random.choice(numbers, 25, replace=False)
        print(randomMembers)
           #choose random points and put them in whitex and whitey
        for x in range(len(randomMembers)):
            whitesx.append(whitesxx[randomMembers[x]])
        for y in range(len(randomMembers)):
            whitesy.append(whitesyy[randomMembers[y]])

        print((whitesx))
        print(whitesy)
         #needed for calculating m
        x2 = []
        for k in range(len(whitesx)):
            x2.append(whitesx[k] * whitesx[k])
        # to calculate xy to find xy bar
        mean_xy_ = []
        for y in range(len(whitesx)):
            mean_xy_.append(whitesx[y] * whitesy[y])
        #calculate m and c
        meanxybar = statistics.mean(mean_xy_)
        m = (((statistics.mean(whitesx)) * (statistics.mean(whitesy))) - meanxybar) / (
            ((statistics.mean(whitesx) * statistics.mean(whitesx))
             - statistics.mean(x2)))
        c = statistics.mean(whitesy) - (m * statistics.mean(whitesx))

        print(m)
        print(c)



        img2 = cv2.line(img, (int(1),int(1*m + c)), (int(40),int(40*m + c)), (255, 255, 0), 1)

        whitesy.clear()
        whitesx.clear()
        whitesxx.clear()
        whitesyy.clear()
    return img2



img2 =Ransac();
cv2.imwrite('lineeeee.jpg',img2)

cv2.imshow('img',img2)
cv2.waitKey(0)
