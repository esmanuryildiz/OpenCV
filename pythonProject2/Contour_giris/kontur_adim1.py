import cv2

img = cv2.imread("2.1 contour1.png.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #resmi gri formata cevirdik

#trashold islemini yapalim:
_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

#kontur koordinatlarını bulalım.
# _ girilen değişkenleri kullanmayacağız.
#cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE kısmını hata almamak için ekliyoruz.
contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#elde ettiğimiz kontur koordinatlarını birleştirip çizim yapalim.
cv2.drawContours(img,contours,0,(0,0,255),3)

cv2.imshow("contour",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

