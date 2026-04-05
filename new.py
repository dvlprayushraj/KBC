import cv2


image = cv2.imread('image.jpg')

if image is None:
   print("image could not load")
   
else:
    (h,w) = image.shape[:2]
    
    center = (w//2,h//2)
    
    m = cv2.getRotationMatrix2D(center,90,1.0)
    rotated = cv2.warpAffine(image,m,(h,w))
    
    cv2.imshow("original show ", image)
    cv2.imshow("rotated image ", rotated)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    