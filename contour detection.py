import numpy as np
import cv2

img = cv2.imread('opencv3.png',)
#img = cv2.resize(img, (600, 600))
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgGray,127,255,0)
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

print('number of contours='+str(len(contours)))
print(contours[0])

cv2.drawContours(img,contours,-1,(0,255,0),3)

#img = cv2.resize(img, (400, 400))
#imgGray = cv2.resize(imgGray, (400, 400))

cv2.imshow('image',img)
cv2.imshow('gray-image',imgGray)

cv2.waitKey(0)
cv2.destroyAllWindows()