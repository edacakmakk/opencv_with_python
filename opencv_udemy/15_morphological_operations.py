import cv2
import numpy as np 

img = cv2.imread("resim.jpg", 0)
kernel = np.ones((5,5), np.uint8)
#erosion = cv2.erode(img, kernel, iterations = 1)
#dilation = cv2.dilate(img, kernel, iterations = 1)
#opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
#closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

cv2.imshow("Original", img)
#cv2.imshow("erosion", erosion)
#cv2.imshow("erosion", dilation)
#cv2.imshow("erosion", opening)
#cv2.imshow("erosion", closing)
#cv2.imshow("erosion", gradient)
cv2.imshow("erosion", tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()
