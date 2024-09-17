import cv2
import numpy as np

img = cv2.imread("15.1 text.png.png")


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #resmi griye cevirdik.

#cv2.goodFeaturesToTrack fonksiyonu 4 parametre alır:gray,maks köşe sayısı,kalite değeri,köşeler arası min mesafe
#Bu fonksiyonu kullanmak için göresi float 32 tipine çevirmem lazım.
gray = np.float32(gray)
corners = cv2.goodFeaturesToTrack(gray,50,0.01,10)

#bulduğumuz köşeleri çizmek için dönüşüm yapıyoruz.
corners = np.int0(corners)

for corner in corners:
    x,y = corner.ravel() #x ve y ye ulaşmak için tek bi satıra dökmek istiyorum.
    cv2.circle(img,(x,y),3,(0,0,255),-1)

cv2.imshow("corner",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

