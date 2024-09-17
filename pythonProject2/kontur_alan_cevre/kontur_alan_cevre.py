import cv2

img = cv2.imread("5.1 contour.png.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255,cv2.THRESH_BINARY) #threshold uyguladık.
contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
area = cv2.contourArea(cnt) #alan bulma fonksiyonu: cnt yi alıyor hesaplıyor ve alanı veriyor.
print(area)
M = cv2.moments(cnt)
print(M['m00'])#M yi hesaplayıp içindeki m00 a ulaşıp yazdırdı. Bu şekildede momentsi kullanarak alan hesapladık.

perimeter = cv2.arcLength(cnt,True) #Şekil kapalıysa hesaplamaya devam et.
print(perimeter)#Koturları alıyor Fonksiyona yerleştiriyor ve çevreyi döndürüyor.



"""
cv2.imshow("original",img)
cv2.imshow("gray",gray)
cv2.imshow("thresh",thresh)


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""