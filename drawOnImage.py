import numpy as np
import cv2
img = cv2.imread('butterfly.jpg',1)
img = np.zeros([512,512,4],np.uint8)
img = cv2.line(img,(0,0),(255,255),(20,100,200),10)

img = cv2.arrowedLine(img,(0,255),(255,0),(140,30,45),5)
img = cv2.rectangle(img,(10,100),(50,200),(0,0,255),-1)
img = cv2.circle(img,(150,150),50,(0,255,0),-1)

font = cv2.FONT_HERSHEY_COMPLEX
line = cv2.LINE_AA
img = cv2.putText(img,'Drawing img',(10,100),font,2,(200,100,100),5,line)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

