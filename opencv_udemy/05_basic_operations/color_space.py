import cv2

img = cv2.imread("resim.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


cv2.imshow("image RGB", img_rgb)
cv2.imshow("image HSV", img_hsv)
cv2.imshow("image GRAY", img_gray)
cv2.imshow("image BGR", img)
cv2.waitKey(0)
cv2.destroyAllWindows()