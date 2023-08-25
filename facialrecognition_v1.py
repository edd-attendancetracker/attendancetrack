#!/usr/bin/env python
from deepface import DeepFace
from picamera import PiCamera
from time import sleep

#creates a number of filepaths used to store pictures taken by the camera

#takes a picture every fifth of a second and places them into one folder
def gather_attendence_pictures():
    camera = PiCamera()
    #while True: 
    #    camera.capture(filepath)
    #    sleep(0.2)
    camera.capture('/home/Downloads/capture.jpg')

gather_attendence_pictures()
