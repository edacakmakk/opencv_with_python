import cv2
import numpy as np

img = cv2.imread("cards.jpeg")

width, height = 250, 350
pts1 = np.float32([[132,346], [357,124], [465,710], [703,489]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))



for x in range(0,4):
    cv2.circle(img, (int(pts1[x][0]), int(pts1[x][1])), 5, (0,0,255), cv2.FILLED)

cv2. imshow("original image", img)
cv2. imshow("output image", imgOutput)

cv2.waitKey(0)
cv2.destroyAllWindows()
