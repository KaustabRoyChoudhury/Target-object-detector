import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# yellow_lower = np.array([22, 93, 0])
# yellow_upper = np.array([45, 255, 255])
sensitivity = 15
lower_white = np.array([0,0,255-sensitivity])
upper_white = np.array([255,sensitivity,255])

while True:
    ret, frame = cap.read()
    vflip=cv2.flip(frame,1)
    #gray=cv2.cvtColor(vflip, cv2.COLOR_BGR2GRAY)
    hsv= cv2.cvtColor(vflip, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_white, upper_white)
    cv2.imshow('My Cam', vflip)
    cv2.imshow('Masked',mask)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()    
cv2.destroyAllWindows()