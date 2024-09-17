import cv2
import numpy as np

canvas=np.zeros((512,512,3), dtype=np.uint8)+255 #canvas ile tuval tanımladım np.zeros ile siyah boş bir tuval oluşturdum.
#.uint8 çizim yaparken kullandığım veri tipidir.
#eğer beyaz bir tuval oluşturmak istiyorsam 255 eklerim.Matris 0 iken siyahtır. Varsayılan siyahtır.


#fonskiyon=çizgi çizmek. Bunun için "line" fonksiyonunu kullanırız.
#geometrik düşünerek hareket ederiz: çizginin bir başlangıç bir de bitiş noktası vardır.
#cv2.line(çizimi yapacağımız yer, çizginin başlangıç noktası,çizginin bitiş noktası,çizginin rengi,çizginin kalınlığı

cv2.line(canvas,(50,50),(512,512),(255,0,0),thickness=5)
cv2.line(canvas,(100,100),(200,250),(0,0,255),thickness=7)








#fonksiyon=dikdörtgen çizmek. Bunun için "rectangle" fonksiyonunu kullanırız.
#geometrik düşünerek hareket edeeriz: dikdörtgenin sol üst köşesi ile sağ alt köşesinin koordinatları verilirse en ve boy oranını buluruz.
#cv2.rectangle(dikdörtgeni yapacağımız yer, sol üst köşe koordinatları,sağ alt köşe kooordinatları,rengi,kalınlığı)

cv2.rectangle(canvas,(20,20),(50,50),(0,255,0), thickness=2)
#dikdörtgenimin içini dolu yapmak için thickness=-1 demem yeterli.
cv2.rectangle(canvas,(30,30),(60,60),(0,255,0), thickness=-1)







#fonksiyon=çember çizmek. Bunun için "circle" fonksiyonunu kullanırız.
#geometrik düşünürsek: çemberin bir merkezi ve bir de yarıçapı vardır.
#cv2.cirle(çemberi yapacağımız yer,merkez noktası,yarıçap değeri,rengi,kalınlığı

cv2.circle(canvas,(250,250),100,(0,0,255),thickness=3)
#çemberin içini doldurmak yani daire yapmak için thickness=-1 demem yeterli.
cv2.circle(canvas,(20,220),10,(0,0,255),thickness=-1)









#fonksiyon: üçgen çizmek. cv2 bunun için bize özel bir fonksiyon vermiyor. Fakrlı yöntemler ile üçgen çizbeiliriz.
#3 adet çizgi çekerek(line) üçgen çizelim:
#üçgein geometrisi: 3 köşe noktası ile cv2.line kullanarak üçgen çizebiliriz.3 koordinatı belirleyelim.

p1=(100,200)
p2=(50,50)
p3=(300,100)
cv2.line(canvas,p1,p2,(0,0,255),thickness=3)
cv2.line(canvas,p2,p3,(0,0,255),thickness=3)
cv2.line(canvas,p3,p1,(0,0,255),thickness=3)








#fonksiyon: çokgen çizmek(dörtgen vs vs) Bunun için "polylines" fonksiyonunu kullanabiliiriz.
#geometrik olarak incelersek: çokgenleri oluşturan çizgileri birlşetirmek.
#cv2.polylines(çizim yapacağım yer,ihtiyacım olan koordinatlar[points], çokgenin kapalı olması için: True, renk,kalınlık)
#False degeri ile çokgen kapanmaz,açık kalır.

points=np.array([[[110,200],[330,200],[290,220],[100,100]]],np.int32) #numpy ile oluşturduğumuz her sayı dizinin veri tipini girmeliyim:np.int32
cv2.polylines(canvas, [points], True,(0,0,255),thickness=5)





#fonksiyon: elips çizmek. Bunun için "ellipse" fonksiyonu kullanılır.
#geometrik olarak ,incelersek: merkez noktası,yatay uzunlupu,dikey uzunluğu
#cv2.ellipse(çizimin yapılacağı yer,merkez noktası,(en,boy,),elipsin yatayla yapacağı açı,elipsin kaç derece başlayıp,kaç derecede biteceği,renk,kalınlık)
cv2.ellipse(canvas,(300,300),(80,20),10,90,360,(255,255,0),thickness=-1)













cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()