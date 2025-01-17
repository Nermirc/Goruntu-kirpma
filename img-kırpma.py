import cv2 

#original

img = cv2.imread("kaplumbaga-terbiyecisi.jpg")
print("Resim boyutu :",img.shape)
cv2.imshow("Orijinal",img)

#resized
imgResized = cv2.resize(img,(800,800))
print("Resized Img Shape",imgResized.shape)
cv2.imshow("Img Resized",imgResized)

#crop
imgCropped = img[:200,:300]
cv2.imshow("Kırpılmış resim",imgCropped)