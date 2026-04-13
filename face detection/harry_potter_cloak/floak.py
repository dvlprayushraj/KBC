import cv2
import numpy as np

cap = cv2.VideoCapture(0)

background_image = cv2.imread('image.jpg')

while cap .isOpened():
    ret,frame = cap.read()
    
    if ret:
        
        #convert RGB INTO HSV COLOR
        hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        
        ##range for hsv color
        
        l_red = np.array([0,120,70])
        u_red = np.array([10,255,255])
        
        
        mask1 = cv2.inRange(hsv_frame,l_red,u_red)
        
        ## range for upper red
        l_red = np.array([170,120,70])
        u_red = np.array([180,255,255])
        
        mask2 = cv2.inRange(hsv_frame,l_red,u_red)
        
        
        
        #generate the final red mark
        
        red_mark = mask1+mask2
        
        
        
        #detect tthe thins that are not red
        
        
        
        #if cloak is not present show the current image 
        
        
        #final output 
        
        
        
        
        
        cv2.imshow("cloak", red_mark)
        if cv2.waitKey(5) == ord('q'):
            break
        
        
    
cap.release()
cv2.destroyAllWindows()


        
        
                