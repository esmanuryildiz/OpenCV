#bu kavram ile resmi en boy oranlarına dikkat ederek açıyor olacağız.
#bu sayede fotoğraf küçülürken orantılı olarak küçülecek veya büyürken orantılı olarak büyüyecek

import cv2
#resmi boyutlandırırken çakışmalar olmasın diye cv2.INTER_AREA kullandık.
def resizewithAspectRatio(img, width=None, height=None, inter=cv2.INTER_AREA):
    dimension=None #boyut için değişken aldık. içini boş bıraktık.
    (h,w)=img.shape[:2] #kullanacağımız resmin içine girdik ve tuple oluşturarak h ye yükseklik w ye en değerini atadık.

    if width is None and height is None: #en ve boy bilgisi verilmemişse
        return img

    if width is None: #boy bilgisi verilmemişse
        r=height/float(h) #kullanıcıdan aldığım boy değerini resmin orijinal boyuna böldüm. floatı daha hassas olması için kullandım.
        dimension=(int(w*r),height)
    else:
        r=width/float(w)

        dimension=(width,int(h*r))

    return cv2.resize(img,dimension,interpolation=inter)

img=cv2.imread("aycicegi.jpg") #fotoğrafı normal olarak çağırdım.
img1=resizewithAspectRatio(img,width=None,height=600,inter=cv2.INTER_AREA)
cv2.imshow("orijinal",img)
cv2.imshow("degistirilmis",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


