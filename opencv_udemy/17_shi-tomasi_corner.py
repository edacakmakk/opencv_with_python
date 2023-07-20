import cv2
import numpy as np

img = cv2.imread("text.png")
img2 = cv2.imread("contour.png")

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 10)
corners = np.int0(corners)
for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img2, (x,y), 3, (0,0,255), -1)

cv2.imshow("corner", img2)




cv2.waitKey(0)
cv2.destroyAllWindows()