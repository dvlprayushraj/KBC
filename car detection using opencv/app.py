import cv2

image = cv2.imread('car detection using opencv\image1.jpg')

resize_image = cv2.resize(image, (0,0),fx=0.2,fy=0.2)



cv2.imshow("image ",resize_image)
cv2.waitKey(0)
cv2.destroyAllWindows()