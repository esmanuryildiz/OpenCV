#Giriş olarak verilen görüntüyü ikili görüntüye çevirmek için kullanılan bir yöntemdir.
# İkili görüntü (binary), görüntünün siyah ve beyaz olarak tanımlanmasıdır.
# Morfolojik operatörler gibi görüntü üzerindeki gürültüleri azaltmak veya nesne belirlemek gibi farklı amaçlar için kullanılır.
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("images.jpeg",0)
ret,th1 = cv2.threshold(img,150,200,cv2.THRESH_BINARY)
#THRESH_BINARY
#Kaynak olarak alınan görüntü üzerindeki piksel,esikDegeri olarak verilen değerden büyükse maksDeger olarak verilen parametre değerine atanır.
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,2)


cv2.imshow("img-th1",th1)
cv2.imshow("img-th2",th2)
cv2.imshow("img-th3",th3)


cv2.waitKey(0)
cv2.destroyAllWindows()

