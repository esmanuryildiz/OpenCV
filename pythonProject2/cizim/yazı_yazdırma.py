#bir tuvale yazı yazdırma.

import cv2
import numpy as np

canvas=np.zeros((512,512,3), dtype=np.uint8)+255


#ekrana yazı yazdırmak için cv2.putText fonksiyonu kullanılır.
#cv2.putText(yazıyı yazacağımız yer,yazı metni,yazının koordinatı,yazı fontu,fontun büyüklüğü,yazının rengi,yazı tipi(cv2.LINE_AA=varsayılan))

font1=cv2.FONT_HERSHEY_COMPLEX
font2=cv2.FONT_ITALIC
font3=cv2.FONT_HERSHEY_SCRIPT_COMPLEX

cv2.putText(canvas,"OpenCv",(50,100),font1,3,(0,0,0),cv2.LINE_AA)
cv2.putText(canvas,"OpenCv",(50,300),font2,3,(0,0,0),cv2.LINE_AA)
cv2.putText(canvas,"OpenCv",(50,500),font3,3,(0,0,0),cv2.LINE_AA)







cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()