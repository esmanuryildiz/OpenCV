import cv2

cap = cv2.VideoCapture(0)
# içerisine gireceğimiz değişken videoyu webcamden mi yoksa bilgisayarda bulunan bir dosyadan mı okuyacağımızı söyler.
# 0 girersek webcami kullanmış oluruz.
# dosyadan video almak için videonun adresini gireriz.

# videoda bütün olarak değişiklik yapamıyoruz. Kareleri üzerinden işlem gerçekleştiriyoruz.Sonsuz döngü açtık;
while True:
    ret, frame = cap.read()
    # kareleri teker teker okumamızı sağlar.
    # iki deger dondurur.ilki Videoları doğru okuduysa true,false.ikincisi framelerdir
    cv2.imshow("webcam", frame)  # while döngüsü döndüğü sürece frameleri okuyacağım. ve imshow ile göstereceğim.
    if cv2.waitKey(30) & 0xFF == ord("q"): #0xFF in karşılığı klavyede q harfidir.ord fonksiyonu ile de q yu klavye bağlantılı yapıyorum.
        break #her frame i 1 milisaniye göster ve q ya bastığımda döngüyü kır,pencereyi kapat.
# her bir frame'i ekrande 30 milisaniye görmemizi sağlar. video kalitesinin bir ölçüsüdür.

cap.release()
# videoyu serbest bırakmamızı sağlar.
cv2.destroyAllwindows
