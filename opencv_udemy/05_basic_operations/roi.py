#roi -> region of interest

import cv2
img = cv2.imread("jack_sparrow.jpg")
#print(img.shape[:2])

roi = img[90:250, 150:300]


cv2.imshow("Jack", img)
cv2.imshow("Roi", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
