import cv2

# capture the video 

cap = cv2.VideoCapture(0)

while cap .isOpened():
    ret, backgroud = cap.read()
    
    if ret:
        cv2.imshow("image",backgroud)
        
        if cv2.waitKey(4) & 0xFF == ord('q'):
            break
            cv2.imwrite("image.jpg ",backgroud)
            
cap.release()
cv2.destroyAllWindows()
    