import cv2

image = cv2.imread('image.jpg')

if image is None:
    print("image load sucessfully")
    
else:
    print("image load failed")
    
    resize_image = cv2.resize(image, (300, 300))
    cv2.imshow("resized image", resize_image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
    
    