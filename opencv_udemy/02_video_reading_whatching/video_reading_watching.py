import cv2

cap = cv2.VideoCapture("video.mp4") # 0 yazarsak wabcamden görüntü alırız

while True:
    ret, frame = cap.read()
    
    if ret == 0: # video bitince döngüden çıkmasını sağlıyor
        break 

    frame = cv2.flip(frame, 1) #videoyu döndürme işlemi | 1 y eksenine göre tersini alır
    cv2.imshow("video", frame)
    if cv2.waitKey(10) & 0xFF == ord("q"): #q ya basıldığında ekranı kapatır.
        break


cap.release()
cv2.destroyAllWindows()