import cv2

cap = cv2.VideoCapture("video.mp4") # If we write 0, we get an image from the wabcam.

while True:
    ret, frame = cap.read()
    
    if ret == 0: # makes the video go out of the loop when it's finished
        break 

    frame = cv2.flip(frame, 1) #rotate video | 1 inverses about the y-axis
    cv2.imshow("video", frame)
    if cv2.waitKey(10) & 0xFF == ord("q"): #Pressing q turns off the screen.
        break


cap.release()
cv2.destroyAllWindows()
