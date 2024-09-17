# cv2.Canny(input,minThreshold,maxThreshold) fonksiyonunu kullanarak kenarları belirleriz.
import cv2

cap = cv2.VideoCapture(0) #webcamden görüntüyü çektik

while 1:
    ret,frame = cap.read() #tüm frameleri okuduk.
    frame = cv2.flip(frame,1)  #flip görüntüyü takla attırır(ben sağ elimi kaldırdığımda görüntününde sağı kalkar)

    edges = cv2.Canny(frame,100,200) #framelerin köşelerini bulduğumuz verileri topladık

    cv2.imshow("Frame",frame)
    cv2.imshow("Edges",edges)

    if cv2.waitKey(5) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()