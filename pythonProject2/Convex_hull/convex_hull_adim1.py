
#CONVEX HULL
#İçbükey şekillere dışbükey örtüler çizmek anlamına gelir(yıldız->içbükey şekil, beşgen->örütüsü)

import cv2
import numpy as np

img=cv2.imread("8.1 map.jpg.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #RESMİ GRİYE DÖNÜŞTÜRDÜK.
blur=cv2.blur(gray,(3,3)) #resmi blurladık,yumuşattık.
ret,thresh=cv2.threshold(blur,40,255,cv2.THRESH_BINARY) #RESMİ binary formata yani siyah beyaz formata cevirdi.

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #konturları bulduk ve contours içinde saklıyoruz.

#kontur noktalarını saklamak için bir dizi oluşturuyorum
hull=[]
#dongu yardımıyla bulduklarımı dizi de saklayacağım.
for i in range(len(contours)): #-0 ve kontur uzunluğu arasındaki sayıları dondurecek
    hull.append(cv2.convexHull(contours[i],False))#False dondurdugu için convexhull değeri değil contours indisini döndürür.
    #hull append bulunan değerleri hull[] içine atacak ve saklayacak.

#bulduğum sonuçları çizmek için siyah bi ekran oluşturuyorum.
bg = np.zeros((thresh.shape[0],thresh.shape[1],3),np.uint8)


for i in range(len(contours)):
    cv2.drawContours(bg,contours,i,(255,0,0),3,8)
    cv2.drawContours(bg,hull,i,(0,255,0),1,8)

cv2.imshow("Image",bg)
cv2.waitKey(0)
cv2.destroyAllWindows()











"""
cv2.imshow("original",img)
cv2.imshow("gray",gray)
cv2.imshow("blur",blur)
cv2.imshow("thresh",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""