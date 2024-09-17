#bir videoda renk uzayını değiştirmek istiyorsak tek seferde tüm videonunkini değiştiremeyiz.
#tek tek frame'leri çekerek renk uzaylarını değiştiririz.

import cv2
#videomuzu okuyoruz;
cap=cv2.VideoCapture("WhatsApp Video 2023-11-01 at 17.05.35.mp4")

while True:
    ret,frame=cap.read()

    #framelerin renk uzaylarını değiştirelim
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #video bitince bittiğini bildirmediğimiz için videoyu izledikten sonra hatayla karşılaşırız;
    if ret==False:
        break

    cv2.imshow("video",frame)
    if cv2.waitKey(30)& 0XFF==ord("q"):
        break


cap.release()
cv2.destroyAllWindows()