import cv2
import numpy as np
img=np.zeros((10,10,3),dtype=np.uint8)
#3 kanal verisi renkli resimler için geçerlidir.

#pikselleri tek tek boyuyarak bir görüntü elde edeceğiz.
img[0,0]=(255,255,255) #pikseller 0.0 dan başlar.
img[0,1]=(255,255,200)
img[0,2]=(255,255,150)
img[0,3]=(255,255,15)



#yukarıda oluşturduğumuz tuvali yeniden boyutlandırmak için;
img=cv2.resize(img,(1000,1000),interpolation=cv2.INTER_AREA)
#interpolation=cv2.INTER_AREA ile bir takım çakışmaları önlemiş oluruz. Varsayılan olarak belirtiriz. resize kullanırken kullanmaya özen gösterelim.

cv2.imshow("canvas",img)
cv2.waitKey(0)
cv2.destroyAllWindows()