import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype = np.uint8) + 55 #sonuna girdiğim sayı rengi değiştiriyor

#print(canvas) --> 


cv2. imshow("canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()


