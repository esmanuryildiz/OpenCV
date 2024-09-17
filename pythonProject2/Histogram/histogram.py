# Histogramı bir görüntünün yoğunluk dağılımı hakkında genel bilgi veren bir grafik veya alan olarak düşünebilirsiniz.
# Histogram görüntüyü analiz etmenin başka bir yoludur.
# Görüntünün histogramına bakılarak o görüntünün parlaklık, kontrast, yoğunluk dağılımı vb. gibi bilgiler elde edinebilirsiniz.

import cv2
import numpy as np
from matplotlib import pyplot as plt
"""
#500 500 boyutlarında siyah bi ekran oluşturalım.
img=np.zeros((500,500),np.uint8)
cv2.rectangle(img,(0,60),(200,150),(255,255,255),-1)
cv2.rectangle(img,(250,170),(350,200),(255,255,255),-1)

plt.hist(img.ravel(),256,[0,256])#histogramımızı çizmeye yarar.ravel ile resmi tek bi satır haline getirir.
"""

img = cv2.imread("14.1 smile.jpg.jpg")

#histogram grafiğini daha iyi okumak için resmin bgr değerlerine ulaşalım.
b,g,r = cv2.split(img) #split resmin bgr değerlerini ayırır.
cv2.imshow("img",img)

plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])


plt.show()#histogramımızı gösrmeye yarar.



cv2.waitKey(0)
cv2.destroyAllWindows()

