#Derin öğrenme ile görüntü işleme üzerinde çalışırken görüntüde açılma, kapatma gibi bir çok morfolojik olay gerçekleştirmek isteriz.
#morfolojik işlemlerden; erezyon
#Erozyon işlemi ön taraftaki nesnenin sınırlarını aşındırmayı sağlar.

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("images.jpeg",0)
kernel = np.ones((5,5),np.uint8)

#morfolojik işlemlerden; erezyon
#Erozyon işlemi ön taraftaki nesnenin sınırlarını aşındırmayı sağlar.
#cv2.erode(resmin adı,matris,iterasyon değeri-tekrarlamak-)
eresion=cv2.erode(img,kernel,iterations=1)

#Genişleme (Dilation)
#Genişleme erozyonun tam tersidir. Aynı şekilde görüntünün üzerinde kutucuk dolaştırarak sağlanır.
# Fakat beyaz yerleri inceltmek yerine kalınlaştırır. Bunu “dilate()” fonksiyonu ile sağlar.
# Bu fonksiyon parametre olarak; işlem yapılacak görüntü, görüntünün üzerinde hareket edecek kutucuk ve ”iterations” değerini alır.
# Bu “iterations” değeri, görüntüye kaç kez genişleme uygulanacağını belirler.
dilation=cv2.dilate(img,kernel,iterations=1)

#Açılma(Opening)
#Açılma işlemi, erozyon ve genişlemenin peş peşe kullanılmasıdır.
# Açılma işleminin yapılma sebebi, eğer görüntünün üzerinde gürültü varsa gürültünün giderilmesine faydalıdır.
# Öncelikle resimdeki beyaz yerleri incelttiğimiz için beyaz gürültüyü yok ederiz
# daha sonra da genişleterek görmek istediğimiz alanı eski haline geri getirmiş oluruz.
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN, kernel)




cv2.imshow("img",img)
cv2.imshow("erosion",eresion)
cv2.imshow("dilation",dilation)
cv2.imshow("opening",opening)
cv2.waitKey(0)
cv2.destroyAllWindows()



