#!/usr/bin/env python

import numpy as np
import cv2
from deepface import DeepFace
from time import sleep

#list of all people's names and their photo directories
roster = {
        "Hagan Riethmiller" : '/home/haozewang/Facial_Recognition/attendancetrack/roster/Hagan_Riethmiller.png',
        "Haoze Wang" : '/home/haozewang/Facial_Recognition/attendancetrack/roster/Haoze_Wang.png'
        }
mugshots = []
cropshots = []

#takes a picture every quarter second and saves it
def collect_pictures():
    #n will determine how many pictures will be taken
    n=0
    # Capture a frame from the camera every 0.25 seconds
    #this will run for 1 seconds
    while n<4:
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
        print(mugshots)
        sleep(0.1)
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
            print(cropshots)
#recursively compares each mugshot to the reference photos to determine who are in the mugshots
def compare_pictures():
    for i in range(len(roster)):
        print(list(roster.values())[i])
        DeepFace.find(img_path = str(list(roster.values())[i]), db_path = '/home/haozewang/Facial_Recognition/attendancetrack/cropped_pictures/', enforce_detection = False)[0]


collect_pictures()
process_pictures()
compare_pictures()
