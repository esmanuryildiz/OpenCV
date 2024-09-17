import cv2
img= cv2.imread("aycicegi.jpg")
#bu fonksiyon ile resimlerin matematiksel değerini okumuş oluruz.2 parametre alır.
#okuma esnasında verilen resmi python dosyası içinde arar. biz başka bir konumdaki fotoğafı eklemek istersek;
#başına istenilen fotoğrafın konumunu ekleriz img= cv2.imread("/Users/esmanuryildiz/Desktop/aycicegi.jpg")
# Birincisi resmin adı olmak zorundadır. İkincisi fotoğrafın okunma şeklidir. ZOrunlu değildir."""
#fotografın okunma şeklini gri yapmak istersek;
#img= cv2.imread("aycicegi.jpg",cv2.IMREAD_GRAYSCALE) yada virgüden sonrası için 0 yazarız.

print(img)
#Çıktı olarak matris alırım. Resimler matrislerden oluşur

cv2.namedWindow("image",cv2.WINDOW_NORMAL)
#açılacak pencerenin adı image. windownormal parametresi sayesinde ise pencerenin boyutu ile ilgili oynama yapabiliyoruz.

cv2.imshow("image",img)
#resmi gösterir.
#2 argüman alır. Birincisi resmin tutulacağı pencerenin adı. İkinciside resmimin tutulduğu değişkendir.
#run yaptığımız zaman resmi anlık görürüz ve kaybederiz. Bunun için bir fonksiyon daha yazarız.

cv2.imwrite("aycicegi1.jpg",img)
#resmi kaydeder
#eger konum belirtmezsek ilgili python dosyasına kaydetme yapar. istediğimiz konuma kaydetmek için konumun yerini belirleyelim.
#cv2.imwrite("/Users/esmanuryildiz/Desktop/aycicegi1.jpg",img)
#ilk parametre resmin tuttulacağı dosyanın adıdır.ikinci parametre kaydedilecek değişkendir.

cv2.waitKey(0)
#içine yazılan değer milisaniyedir. 0 yazarsak biz kapatana kadar ekranda kalır. image isimli pencere ile açılır.

cv2.destroyAllWindow()
#bu fonksiyon ise tüm pencereleri kapamaya yarar. Karmaşıklığı önlemek için kullanımı önemlidir.
