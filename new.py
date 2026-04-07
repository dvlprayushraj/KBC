import cv2

# 1. Initialize the camera (0 is usually the default built-in camera)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # 2. Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly, ret is True
    if not ret:
        print("Error: Can't receive frame. Exiting...")
        break

    # 3. Display the resulting frame in a window named 'Camera Feed'
    cv2.imshow('Camera Feed', frame)

    # 4. Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 5. Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
