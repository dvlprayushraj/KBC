import cv2

image = cv2.imread('image.jpg')


if image is  not None:
    cv2.imshow("image showing ", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image read successfully.")