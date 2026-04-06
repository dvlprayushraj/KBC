import cv2

image = cv2.imread(input("enter your image location / formate to display your image : "))



if image is not None:
   
   print("image loade sucessfully")
   


   cv2.waitKey(0)
   cv2.destroyAllWindows()
   
   
   
   
   user_choice = str(input("what do you wnat to draw on the image \n  1. LINE \n 2. CIRCLE \n 3. RECTANGLE \n 4. TEXT\n\n\n"))

### user want to draw a line




   
   if user_choice == "line":
   
      pt1 =(50,100)
      pt2 =(300,100)
      thickness = 5
      color = (0,0,255)
   
      happt = cv2.line(image,pt1,pt2,color,thickness)
      cv2.imshow("your image", happt)
      cv2.waitKey(0)
      cv2.destroyAllWindows()
   
   ## if user want to draw an circle 
   
   if user_choice == "circle":
      center =(200,200)
      radius = 30
      color = (0,0,255)
      thickness = 5
   
      circle = cv2.circle(image,center,radius,color,thickness)
      cv2.imshow("here is you circle drawn",circle)
      cv2.waitKey(0)
      cv2.destroyAllWindows()
      
   if user_choice == "rectangle":
      pt1 =(50,100)
      pt2 =(300,10)
      color = (0,0,255)
      thickness = 5
      
      
      rectangle = cv2.rectangle(image,pt1,pt2,color,thickness)
      cv2.imshow("rectangle image ", rectangle)
      cv2.waitKey(0)
      cv2.destroyAllWindows()
      