import cv2
import numpy as np

img = cv2.imread("14.1 smile.jpg.jpg",0)
row,col = img.shape #shape satır ve sütun sayılarını verir.

#2 boyutta bi yön değiştirme için cv2.getRotationMatrix2D kullanırız. sütun,satır,ölçek değerleirni alır.
M= cv2.getRotationMatrix2D((col/2,row/2),90,1)
dst = cv2.warpAffine(img,M,(col,row))

cv2.imshow("dst",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

