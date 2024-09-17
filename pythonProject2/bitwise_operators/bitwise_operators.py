#OpenCV kütüphanesi, bitwise işlemlerini yapmak için cv2.bitwise_and(), cv2.bitwise_or(), cv2.bitwise_xor() ve cv2.bitwise_not() gibi
# bir dizi işlev sağlar. Bu işlevler, iki veya daha fazla görüntü arasında bitwise işlemleri yapmak için kullanılabilir.
# Bu işlemler, görüntülerin piksel değerlerine dayalı olarak gerçekleştirilir.
#Bitsel işlemler ikili sayı sisteminde bitler üzerinde yapılan mantıksal işlemlerdir.

import cv2
import numpy as np

img1 = cv2.imread("9.2 bitwise_1.png.png")
img2 = cv2.imread("9.1 bitwise_2.png.png")

#resmin siyah yerleri 0 beyaz yerleri 1 dir.
# iki resim üzerindeki siyah ve beyaz yerler ve bağlacı ile bağlanırsa 0 yani siyah sonucu verir.
bit_and = cv2.bitwise_and(img2,img1)
bit_or = cv2.bitwise_or(img2,img1)
bit_xor = cv2.bitwise_xor(img2,img1)
bit_not = cv2.bitwise_not(img1)
bit_not2 = cv2.bitwise_not(img2)



cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("bit_xor",bit_xor)


cv2.waitKey(0)
cv2.destroyAllWindows()






