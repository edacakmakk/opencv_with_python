import cv2
import numpy as np

cap = cv2.VideoCapture("line.mp4")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([18, 94, 140], np.uint8)
    upper_yellow = np.array([48, 255, 255], np.uint8)
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    edges = cv2.Canny(mask, 75, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap = 50)

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1,y1), (x2,y2), (0, 255, 0), 5)
    

    cv2.imshow("img", frame)

    if cv2.waitKey(10) & 0xFF == ord("q"): 
            break

cap.release()
cv2.destroyAllWindows()