#Renk uzayı, renkleri tanımlamak için kullanılan bir koordinat sistemi veya matematiksel modeldir.
#Renk uzayları, belirli bir renk aralığını temsil etmek için kullanılır.
#Her renk uzayı, farklı renkleri temsil etmek için farklı bir yöntem kullanır.
#Renk uzayları, RGB, CMYK, HSL, HSV ve Lab gibi çeşitli türlerde gelir.

import cv2
img=cv2.imread("aycicegi1.jpg")

#Mevcut resmimimi RGB renk uzayı ile görüntüleyelim.
#resimlerin renk uzaylarını değiştirmekiçin kullandığımız fonksiyon; cv2.cvtColor()
imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #bgr dan rgb ye dönüşüm
imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


cv2.imshow("aycicegi bgr",img)
cv2.imshow("aycicegi rgb",imgrgb)
cv2.imshow("aycicegi HSV",imghsv)
cv2.imshow("aycicegi gray",img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()