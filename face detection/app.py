import cv2 

fcae_detection = cv2.CascadeClassifier("face detection\haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces = fcae_detection.detectMultiScale(grey,1.1,5)
    
    for(x,y,w,h) in faces :
        cv2.rectangle(frame,(x,y),(x+w ,y+h),(0,255,0),3)
    
    
    cv2.imshow("webcmae are open",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

