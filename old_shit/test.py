#!/usr/bin/env python
import cv2
from deepface import DeepFace
from time import sleep

#list of all people's names and their photo directories
roster = {
        "Hagan Riethmiller" : '/home/haozewang/Pictures/Webcam/Hagan_Riethmiller.jpg'
        }
mugshots = []

#takes a picture every quarter second and saves it
def collect_pictures():
    # Set up the camera
    cap = cv2.VideoCapture(0)
    # Check if the camera was opened successfully
    if not cap.isOpened():
        raise Exception("Could not open camera")
    #n will determine how many pictures will be taken
    n=0
    # Capture a frame from the camera every 0.25 seconds
    #this will run for 1 seconds
    while n<4:
        ret, frame = cap.read()
        sleep(0.25)
        # Check if the frame was captured successfully
        if not ret:
            raise Exception("Could not capture frame")
        # Save the captured frame to an image file
        cv2.imwrite('image'+str(n)+'.jpg', frame)
        mugshots.append('image'+str(n)+'.jpg')
        n+=1
    # Release the camera and destroy all windows
    cap.release()
    cv2.destroyAllWindows()

#processes the location of the face in each picture taken
def process_pictures():
    for n in roster:
        detected_face = DeepFace.detectFace(mugshots(n))
        cv2.imwrite('cropped_face'+str(n)+'.jpg', detected_face)

collect_pictures()
process_pictures()

