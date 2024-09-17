#roi>>region of interest>>ilgi alanı
import cv2

img=cv2.imread("aycicegi1.jpg")

print((img.shape[:2]))#resmin ne kadarlık olduğunu gördük.

roi=img[300:1400,650:2200]

cv2.imshow("Aycicegi",img)
cv2.imshow("ROi",roi) #roiyi ekrana gösterdik.
cv2.waitKey(0)
cv2.destroyAllWindows()