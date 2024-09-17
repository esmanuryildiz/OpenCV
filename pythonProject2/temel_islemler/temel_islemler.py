import cv2
import numpy as np

img=cv2.imread("aycicegi1.jpg")

#herhangi bir pikselin renk degerine ulasmak icin color degiskeni oluşturdum.
#color=img[150,200] #img resminin 150 200 pikselindeki rengi tuttu.
#print( color)
#resmin kaça kaçlık olduğunu öğrenmek için;
dimension=img.shape
print(dimension) #(1500, 2250, 3)

#herhangi bir pikselin renk degerlerini oluşturalım.
color=img[420,500]
print("BGR:", color)

blue=img[420,500,0]
print("blue:",blue)

green=img[420,500,1]
print("green:",green)

red=img[420,500,2]
print("red",red)


#istediğimiz yerdeki renk değerini değiştirelim.
img[420,500,0]=250
print("new blue:",img[420,500,0])
#başka bir yöntem kullanacak olursak
blue1=img.item(150,200,0) #150 200 piksellerindeki mavi değer
print("blue1:",blue1)
img.itemset((150,200,0),172)
print("new blue:",img[150,200,0])




cv2.imshow("aycicegi",img)
cv2.waitKey(0)
cv2.destroyAllWindows()