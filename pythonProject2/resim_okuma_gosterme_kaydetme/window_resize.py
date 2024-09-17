import cv2
img= cv2.imread("aycicegi.jpg")
cv2.namedWindow("cicek",cv2.WINDOW_NORMAL) #bu sayede resmin boyutunu değiştirebiliyorum.

#ama özel olarak bi boyutta karşıma gelmesizini istiyorsam cv2.resize() kullanmalıyım.
img=cv2.resize(img,(640,480)) #parametre olarak değişkenimi ve istediğim boyutları girdim.


cv2.imshow("cicek",img)
cv2.waitKey(0)
cv2.destroyAllWindows()