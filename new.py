import cv2


image = cv2.imread('flower.png')

image = cv2.resize(image,(0,0),fx=0.3,fy=0.3)

cv2.imshow("original image ",image)

canny_image = cv2.Canny(image, 100,200)

cv2.imshow("canny image", canny_image)
cv2.waitKey(0)
cv2.destroyAllWindows()