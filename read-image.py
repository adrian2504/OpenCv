# read an image

import cv2
img = cv2.imread('butterfly.jpg', 1)

cv2.imshow('image', img)
k= cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('butterfly_copy.jpg', img)
    cv2.destroyAllWindows()