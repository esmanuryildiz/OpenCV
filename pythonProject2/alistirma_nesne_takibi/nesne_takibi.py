import cv2
import numpy as np

cap = cv2.VideoCapture("4.2 dog.mp4.mp4")

while 1:

    _, frame = cap.read()

    # resimlerim rgb şeklinde tutuluyor. Nesne takibini hsv formatında yapabiliyorum.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # videodaki beyaz nesneyi takip edeceğiz.Bunun için bir hsv aralığı belirlemeliyiz.
    # internetten beyaz renk için olan hsv aralığını alabilirsin.
    sensitivity = 15
    lower_white = np.array([0, 0, 255 - sensitivity])
    upper_white = np.array([255, sensitivity, 255])
    mask = cv2.inRange(hsv, lower_white, upper_white)#maske uyguladık. hsv ye cevirdiğim frameleri upper ve lower arasına maske uygula geri kalanı sil.
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

