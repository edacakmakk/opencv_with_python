import cv2
#resim = 'C:\\Users\\edaca\\opencv_udemy\\image_reading_showing_saving\\resim.jpg'
img = cv2.imread("resim1.jpg", 0)
# print(img)
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", img) #allows us to view the image
cv2.imwrite("resim1.jpg", img)
cv2.waitKey(0) #akeeps the popup open until we close it
cv2.destroyAllWindows()

