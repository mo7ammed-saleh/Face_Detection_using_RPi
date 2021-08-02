import numpy as np
import cv2
cap = cv2.VideoCapture(0) #capture the video from pi camera (if we have an mp4 file just set 0 to the path of the video file)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

while(True):
    #Get each frame from the video by cap.read()>(return 2 variable, ret: is a boolean variable that returns true if the frame is available. frame: is an image array vector captured based on the default frames per second )
    ret, frame = cap.read()
    # Flip camera vertically
    frame = cv2.flip(frame, -1)
    #convert to gray scale 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    
    cv2.imshow('frame', frame) #show the frame in BGR color
    cv2.imshow('gray', gray) #show the frame in gray color
    
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit and break if ESC pressed
        break
cap.release()
cv2.destroyAllWindows()
