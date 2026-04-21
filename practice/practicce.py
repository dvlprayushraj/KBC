import cv2

image_recoginer = cv2.CascadeClassifier("practice\haarcascade_frontalface_default.xml")

image = cv2.imread('practice\IMG_20250629_172135.jpg')

resize_image = cv2.resize(image,(0,0),fx=0.2, fy=0.2)


grey = cv2.cvtColor(resize_image,cv2.COLOR_BGR2GRAY)

faces = image_recoginer.detectMultiScale(grey,1.1,4)

for x,y,w,h in faces:
    rectange = cv2.rectangle(resize_image,(x,y),(x+w,y+h),(255,0,0),4)
    

cv2.imshow("image ", resize_image)

if cv2.waitKey(0) & 0xFF == ord('q')
break


cv2.destroyAllWindows()