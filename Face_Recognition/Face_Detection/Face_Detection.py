import numpy as np
import cv2

#load the face detection classifier from your path (classifier path directory)
faceCascade = cv2.CascadeClassifier('/home/pi/opencv/data/haarcascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(1) #capture the video from pi camera (if we have an mp4 file just set 0 to the path of the video file)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

#Set our camera and inside the loop, load our input video in grayscale mode
while True:
    #Get each frame from the video by cap.read()>(return 2 variable, ret: is a boolean variable that returns true if the frame is available. frame: is an image array vector captured based on the default frames per second )
    ret, frame = cap.read()
    frame = cv2.flip(frame, -1) # Flip camera vertically
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert to gray scale 
    
    #detect the faces by call our classifier function, passing it some very important parameters, as scale factor, number of neighbors and minimum size of the detected face.
    faces = faceCascade.detectMultiScale(
        gray, #Matrix containing an image where objects are detected.    
        scaleFactor=1.2, #Parameter specifying how much the image size is reduced at each image scale.
        minNeighbors=5,  #Parameter specifying how many neighbors each candidate rectangle should have to retain it(A higher number gives lower false positives)
        minSize=(20, 20) #Minimum possible object size. Objects smaller than that are ignored.
    )
    #Mark the faces in the image by drawing a blue rect in each face detected 
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2) 
        roi_gray = gray[y:y+h, x:x+w] #roi: rectangular region of interest 
        roi_color = frame[y:y+h, x:x+w]  
        #If faces are found, it returns the positions of detected faces as a rectangle with the left up corner (x,y) and having "w" as its Width and "h" as its Height of the face==> (x,y,w,h)
        
    cv2.imshow('Face Detection',frame) #show the faces
    
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()
