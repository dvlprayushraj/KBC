import cv2

image_location = input("Enter the location of the image: ")

if image_location is not None:
    image = cv2.imread(image_location)
    
    cv2.waitKey(0)
    
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.waitKey(0)
    
user_choice = input("do you want to save or show the iamge ?// ")

if user_choice == "save":
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("grey_image.jpg", grey)
    cv2.imshow("image",image)
    print("Image saved successfully.")

if user_choice == "show":
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("grey ",grey)
    cv2.waitKey(0)
    

