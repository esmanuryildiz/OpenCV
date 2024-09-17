#agirlikli toplma görüntüleri belirli yoğunluklarla birbirleri üzerine eklemeye verilen isimdir.
#F(x,y)=x*a+y*b+c  x i a yoğunluğunda kattık, y yi b yoğunluğunda kattık ve bunları c sabitiyle topladık.
#AGİRLİKLİ TOPLAMADAKİ Mantık budur.


import cv2
import numpy as np

#aynı boyutlu görüntüleri kendimiz oluşturacağız.

#resmimiz diksörtgen.
rectangle=np.zeros((512,512,3),np.uint8)+255
cv2.rectangle(rectangle,(150,150),(350,350),(0,0,250),-1)



#resmimiz tuval ve ortasında bir daire.
circle=np.zeros((512,512,3),np.uint8)+255
cv2.circle(circle,(256,256),60,(255,0,0),-1)


#agirlikli toplama için cv2.addWeighted(toplayacağımız ilk resim,hangi oranda olacağı,toplayacağımız ikinci resim,hangi oranda olacağı)
dst=cv2.addWeighted(circle,0.7,rectangle,0.3,0)


cv2.imshow("rectangle",rectangle)
cv2.imshow("circle",circle)
cv2.imshow("dst",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()