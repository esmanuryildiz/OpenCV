import cv2
import numpy as np
import requests
url="http://10.60.212.211:8080//shot.jpg"
while True:
    img_resp = requests.get(url) #Görüntüyü alacağım url yi değişkenb içinde tutuyorum
    img_arr=np.array(bytearray(img_resp.content), dtype=np.uint8)#aldığım görüntüyü bi array içerisinde turuyorum
    # img_resp.content ile aldığım görüntüyü bytearray'e çevirdim.
    img=cv2.imdecode(img_arr ,cv2.IMREAD_COLOR)#hafızadan çektiğim görüntüyü görüntülenebilir hale getirecek.
    # cv2.IMREAD_COLOR ile görüntü renkli hale gelecek.
    img=cv2.resize(img,(640,480))#görüntümü yeniden boyutlandırdım.
    cv2.imshow("android camera",img)

    if cv2.waitKey(1) == 27:
        break
    cv2.destroyAllWindows()


