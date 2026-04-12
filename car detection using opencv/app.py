import cv2

Img = cv2.imread("modi.jpg")

resize_image = cv2.resize(Img,(0,0),fx=0.2,fy=0.2)

cv2.imshow("image ", resize_image)
cv2.waitKey(0)