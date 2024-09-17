import cv2
cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)


fileName="/Users/esmanuryildiz/udemy/pythonProject2/webcam.avi" #olusturulan dosyanın adını uzantısıyla birlikte girmemiz çok öenmlidir
codec=cv2.VideoWriter_fourcc('W','M','V','2')
frameRate=30
resolution=(640,480)
videoFileOutput=cv2.VideoWriter(fileName,codec,frameRate,resolution)
#videolar ses ve görüntülerden oluşur. bu ses ve görüntüleri birleştirmek için algoritmalar kullanılır. codec bu algoritmaları tanır.
#bu değişken sayesinde frameleri tek tek yazdırırız. 4 degisken alır.
#frameleri okuduktan sonra dosya biçinde kaydetmemiz gerekiyor.
#frame rate=frame oranı
#resolution=cozunurluk


while True:
    ret, frame = cap.read()
    if not ret:
        print("Kamera çerçevesi alınamadı.")
        break
    if ret:
        frame = cv2.flip(frame, 1)
        videoFileOutput.write(frame)
        cv2.imshow("Webcam Live", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

videoFileOutput.release()
cap.release()
cv2.destroyAllWindows()

