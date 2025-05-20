    import cv2
import numpy as np
# Load the virtual background image
background = cv2.imread("background.jpg")
background = cv2.resize(background, (640, 480))  # Resize to match frame size
# Start video capture (0 for default camera)
cap = cv2.VideoCapture(0)
while True:
   ret, frame = cap.read()
            if not ret:
                    break
 frame = cv2.resize(frame, (640, 480))  # Resize to match background
 # Convert the frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 # Define the green screen color range in HSV
        lower_green = np.array([35, 40, 40])
       upper_green = np.array([85, 255, 255])
 # Create a mask where green colors are detected
        mask = cv2.inRange(hsv, lower_green, upper_green)
 # Invert mask to get the foreground
        mask_inv = cv2.bitwise_not(mask)
# Extract the background where mask is white
        bg_part = cv2.bitwise_and(background, background, mask=mask)
# Extract the foreground from original frame
        fg_part = cv2.bitwise_and(frame, frame, mask=mask_inv)
 # Combine both parts
        combined = cv2.add(bg_part, fg_part)
 # Show the result
        cv2.imshow("Virtual Background", combined)
 if cv2.waitKey(1) & 0xFF == ord('q'):
 break
cap.release()
cv2.destroyAllWindows()
