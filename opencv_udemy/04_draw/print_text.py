import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype = np.uint8) + 255 #sonuna girdiğim sayı rengi değiştiriyor

font1 = cv2.FONT_HERSHEY_COMPLEX
font2 = cv2.FONT_HERSHEY_COMPLEX_SMALL
font3 = cv2.FONT_HERSHEY_PLAIN

cv2.putText(canvas, "OpenCV", (100, 100), font3, 2, (0,0,0), cv2.LINE_AA)




cv2. imshow("canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()