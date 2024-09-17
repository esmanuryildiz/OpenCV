import cv2
import numpy as np

font=cv2.FONT_HERSHEY_SIMPLEX
font1=cv2.FONT_HERSHEY_COMPLEX

img=cv2.imread("1.1 polygons.png.png")
#konturları bulmak için önce griye çeviriyoruz. daha sonra trshold uyguluyoruz ve daha sonra konturları buluyoruz.
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,threshold=cv2.threshold(gray,240,255,cv2.THRESH_BINARY)#THRESHOLD uyguladıktan sonra resmi binary e çevirdim.


contours,_=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE #OpenCV kütüphanesindeki cv2.findContours() işlevinin bir parametresidir. Bu parametre, kontur algılama işleminde kullanılan kontur bulma yöntemini belirtir.



#Bu kod, bir görüntüdeki konturları bulmayı ve bu konturları basitleştirerek çizmeyi amaçlar.
for cnt in contours:
     epsilon=0.01*cv2.arcLength(cnt,True) #Konturun uzunluğunu hesaplar.
     approx=cv2.approxPolyDP(cnt,epsilon,True) #cv2.approxPolyDP(): Konturu basitleştirir. Bu, daha az sayıda nokta kullanarak daha düzgün bir kontur sağlar.

     cv2.drawContours(img,[approx],0,(0),5)#cv2.drawContours(): Basitleştirilmiş konturu çizer. Bu, basitleştirilmiş konturu görüntü üzerine çizmek için kullanılır.


     #approx.ravel()[0] ifadesi, düzleştirilmiş konturun ilk noktasının x koordinatını döndürür.
     # approx.ravel()[1] ifadesi ise ilk noktanın y koordinatını döndürür.
     #Bu işlem, basitçe konturun başlangıç noktasının (x, y) koordinatlarını elde etmek için kullanılır.
     x=approx.ravel()[0]
     y=approx.ravel()[1]

     #approx countour'ün basitleştirilmiş halidir.min sayıda nokta ile çizilir.
     #len(approx) köşe sayısını verir gibi düşünebiliriz.
     #org: Metnin sol üst köşesinin koordinatlarıdır (x, y). Bu, metnin başlangıç konumunu belirtir.
     if len(approx) == 3:
         cv2.putText(img, "Triangle", (x, y), font1, 1, (0))

     elif len(approx) == 4:
         cv2.putText(img, "Rectangle", (x, y), font1, 1, (0))

     elif len(approx) == 5:
         cv2.putText(img, "Pentagon", (x, y), font1, 1, (0))

     elif len(approx) == 6:
         cv2.putText(img, "Hexagon", (x, y), font1, 1, (0))

     else:
         cv2.putText(img, "Ellipse", (x, y), font1, 1, (0))



cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()