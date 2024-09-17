import cv2
import numpy as np

img =cv2.imread("9.1 star.png.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(gray,127,255,0)

contours,_ = cv2.findContours(thresh,2,1)
cnt = contours[0]

hull =cv2.convexHull(cnt, returnPoints = False)
defects = cv2.convexityDefects(cnt,hull) #KUSURLARI ARIYORUM:KONTURLAR(CNT),HULL DEĞİŞKENİ İÇİNDE TUTULANLAR.

for i in range(defects.shape[0]):
    s, e, f, d = defects[i,0] #d=distance->uzaklık
    start = tuple(cnt[s][0]) #UÇ NOKTALardan yıldızın başlangıcı
    end = tuple(cnt[e][0]) #son nokta
    far = tuple(cnt[f][0]) #en uzak nokta
    cv2.line(img,start,end,[0,255,0],2)
    cv2.circle(img,far,5,[0,255,0],-1)


cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()