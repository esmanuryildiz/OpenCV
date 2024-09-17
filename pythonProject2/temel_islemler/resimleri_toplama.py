#resimlerde toplama işlemi yapabilrmek için aynı boyutlu(matrisli) görüntülere ihtiyaç vardır.

import cv2
import numpy as np

#aynı boyutlu görüntüleri kendimiz oluşturacağız.

#resmimiz diksörtgen.
rectangle=np.zeros((512,512,3),np.uint8)+255
cv2.rectangle(rectangle,(150,150),(350,350),(0,0,250),-1)
cv2.imshow("rectangle",rectangle)


#resmimiz tuval ve ortasında bir daire.
circle=np.zeros((512,512,3),np.uint8)+255
cv2.circle(circle,(256,256),60,(255,0,0),-1)
cv2.imshow("circle",circle)

#resimlerimizi toplamak için cv2.add fonksiyonu kullanıyoruz.
add=cv2.add(circle,rectangle)
cv2.imshow("add",add)

cv2.waitKey(0)
cv2.destroyAllWindows()