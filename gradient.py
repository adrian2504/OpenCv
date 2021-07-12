import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('gradient1.jpg',0)
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,th2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,th3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)


# display using opencv
#cv2.imshow("image",img)
#cv2.imshow("thresh1",th1)
#cv2.imshow("thresh2",th2)
#cv2.imshow("thresh3",th3)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#display using matplotlib

titles = ['IMAGE', 'BINARY','BINARY_INVERSE','TRUNCATE']
images = [img, th1,th2,th3]

for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()