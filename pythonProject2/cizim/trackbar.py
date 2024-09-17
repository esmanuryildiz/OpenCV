#trackbarı pencere rengi değiştirirken kullanacağız.

import cv2
import numpy as np

#boş bir pencere oluşturdurk:
def nothing(x):
    pass

#pencere rengi değiştirebilmek için önce penceremiz olmalı:
img=np.zeros((512,512,3),np.uint8,)
#trackbar ile oluşturduğumuz pencerenin aynı yerde olması için pencereye isim tanımlıyoruz.
cv2.namedWindow("image")


#trackbar'ımızı cv2.createTrackbar() ile oluşturuyoruz.
#cv2.createTrackbar(kızağın adı,kızağın yerleşeceği pencere adı,kızağın başlangıç, bitişi,oluşturduğumuz boş fonksiyon)
cv2.createTrackbar("R","image",0,255,nothing)
cv2.createTrackbar("G","image",0,255,nothing)
cv2.createTrackbar("B","image",0,255,nothing)

#trackbarı açıp kapatmak için switch değeri oluşturuyoruz.
switch=" 0: OFF , 1:ON"
cv2.createTrackbar(switch,"image",0,1,nothing)


#Trackbara renk eklemek istiyorum fakat trackbarı sürekli kaydırdığım için hep bir dğeişiklik söz konusu.While döngüsü ile yapalım
while True:
    #pencereyi görmek ve q ya basınca ekrandan çıkmak için:
    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xF==ord("q"):
        break


    #cv2.getTrackbarpos() ile kızakların konumlarını alacağız.
    # cv2.getTrackbarpos(kızağın adı,kızağın bulunacağı pencere)
    #alacağımız değerleri bir değişken içinde saklayalım.

    r=cv2.getTrackbarPos("R","image")
    g=cv2.getTrackbarPos("G","image")
    b=cv2.getTrackbarPos("B","image")
    s=cv2.getTrackbarPos(switch,"image")


    #switche görev atayalım.
    if s==0:
        img[:]==[0,0,0]
    if s==1:
        # alacağımız değişkenleri pencereye gönder
        # img[:] img nin tüm piksel değerline ulaşmak anlamına gelir.
        img[:] = [b, g, r]





cv2.destroyAllWindows()











