import cv2
import numpy as np
import requests

url = "http://192.168.1.158:8080//shot.jpg" #The image url we obtained thanks to the IP webcam application

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype = np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (640, 480))

    cv2.imshow("Android camera", img)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
