#burdada bilgisayarımızdan bir video alacağız.
import cv2

cap = cv2.VideoCapture("WhatsApp Video 2023-11-01 at 17.05.35.mp4")
while True:
    ret, frame = cap.read()
    if ret==0: #video sonsuza kadar sürmüyor. video bitmiştir anlamına gelir.
        break


    cv2.imshow("lise", frame)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()

cv2.destroyAllwindow