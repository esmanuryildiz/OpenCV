import cv2
import numpy as np


#bu çalışmada trackbar kullanacağız
def nothing (x):
    pass


#videomuzu çağırıyoruz.
cap=cv2.VideoCapture(0)
cv2.namedWindow("Settings") # işlevi, bir görüntü için bir pencere oluşturmanın bir yoludur.


#Bu trackbar'lar genellikle renk sınırlarını ayarlamak için kullanılır. Örneğin, bir nesnenin rengini belirlemek için alt ve üst sınırları ayarlamak için kullanılabilirler. Bu trackbar'lar, kullanıcının belirli bir uygulamada dinamik olarak renk sınırlarını ayarlamasına olanak tanır.
cv2.createTrackbar("Lower-Hue","Settings",0,180,nothing)
cv2.createTrackbar("Lower-Saturation","Settings",0,255,nothing)
cv2.createTrackbar("Lower-Value","Settings",0,255,nothing)
cv2.createTrackbar("Upper-Hue","Settings",0,180,nothing)
cv2.createTrackbar("Upper-Saturation","Settings",0,255,nothing)
cv2.createTrackbar("Upper-Value","Settings",0,255,nothing)
#Beşinci parametre, trackbar değeri değiştiğinde çağrılacak olan bir geri çağrı işlevidir. Bu örnekte, nothing adlı bir işlev belirtilmiş. Bu işlev, herhangi bir şey yapmayan bir işlevidir (yalnızca pass ifadesini içerir). Trackbar değeri değiştiğinde yapılacak özel bir işlem olmadığında kullanışlıdır.


font=cv2.FONT_HERSHEY_SIMPLEX

while 1:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("Lower-Hue","Settings")
    ls = cv2.getTrackbarPos("Lower-Saturation","Settings")
    lv = cv2.getTrackbarPos("Lower-Value","Settings")
    uh = cv2.getTrackbarPos("Upper-Hue","Settings")
    us = cv2.getTrackbarPos("Upper-Saturation","Settings")
    uv = cv2.getTrackbarPos("Upper-Value","Settings")

