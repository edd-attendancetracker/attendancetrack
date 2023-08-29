#!/usr/bin/env python

import numpy as np
import cv2
from deepface import DeepFace
from time import sleep

#list of all people's names and their photo directories
roster = {
        "Hagan Riethmiller" : '/home/haozewang/Facial_Recognition/attendancetrack/roster/Hagan_Riethmiller.jpg',
        "Haoze Wang" : '/home/haozewang/Facial_Recognition/attendancetrack/roster/Haoze_Wang.png',
        "Jadon Lee" : '/home/haozewang/Facial_Recognition/attendancetrack/roster/Jadon Lee.jpg',
        "Jeremy Suen" : '/home/haozewang/Facial_Recognition/attendancetrack/roster/Jeremy_Suen.jpg',
        #"Keshav Sreekantham" : '/home/haozewang/Facial_Recognition/attendancetrack/roster/Keshav_Sreekantham.jpg', 
        #"Nikhil Modak" : '/home/haozewang/Facial_Recognition/attendancetrack/roster/Nikhil_Modak.jpg',
        "Sofia Davila Ramirez" : '/home/haozewang/Facial_Recognition/attendancetrack/roster/Sofia_Davilaramirez.jpg',
        "Mannat Ahluwalia" : '/home/haozewang/Facial_Recognition/attendancetrack/roster/Mannat_Ahluwalia.jpg'
        }
mugshots = []
cropshots = []

#takes a picture every quarter second and saves it
def collect_pictures():
    #n will determine how many pictures will be taken
    n=0
    # Capture a frame from the camera every 0.25 seconds
    #this will run for 1 seconds
    while n<3:
        print('taking picture in 5')
        sleep(1)
        print('taking picture in 4')
        sleep(1)
        print('taking picture in 3')
        sleep(1)
        print('taking picture in 2')
        sleep(1)
        print('taking picture in 1')
        sleep(1)
        print('smile :)')
         # Set up the camera
        cap = cv2.VideoCapture(0)
        # Check if the camera was opened successfully
        if not cap.isOpened():
            raise Exception("Could not open camera")
        ret, frame = cap.read()
        # Check if the frame was captured successfully
        if not ret:
            raise Exception("Could not capture frame")
        # Save the captured frame to an image file
        cv2.imwrite('/home/haozewang/Facial_Recognition/attendancetrack/webcam_pictures/image'+str(n)+'.jpg', frame)
        mugshots.append('/home/haozewang/Facial_Recognition/attendancetrack/webcam_pictures/image'+str(n)+'.jpg')
        n+=1
        #print(mugshots)      
        # Release the camera and destroy all windows
        cap.release()
        cv2.destroyAllWindows()

#processes the location of the face in each picture taken
def process_pictures():
    for i in range(len(mugshots)):
        detected_faces = DeepFace.extract_faces(mugshots[i])
        for j, face_info in enumerate(detected_faces):
            face = face_info['face']
            # Convert the image data to 8-bit format
            face = np.uint8(face * 255)
            cv2.imwrite('/home/haozewang/Facial_Recognition/attendancetrack/cropped_pictures/cropped_face{}_{}.jpg'.format(i, j), face)
            cropshots.append('/home/haozewang/Facial_Recognition/attendancetrack/cropped_pictures/cropped_face{}_{}.jpg'.format(i,j))
            #print(cropshots)
#recursively compares each mugshot to the reference photos to determine who are in the mugshots
def compare_pictures():
    for i in range(len(roster)):
        print(list(roster.values())[i])
        result = DeepFace.find(img_path = str(list(roster.values())[i]), db_path = '/home/haozewang/Facial_Recognition/attendancetrack/cropped_pictures/', enforce_detection=False)[0]
        print(list(roster.keys())[i]+':')
        print(result)

collect_pictures()
#process_pictures()
compare_pictures()
