#!/usr/bin/env python
#import pickle
import pandas as pd

#with open('/home/haozewang/Facial_Recognition/attendancetrack/pictures/representations_vgg_face.pkl', 'rb') as f:
#    data = pickle.load(f)
df = pd.read_pickle('/home/haozewang/Facial_Recognition/attendancetrack/cropped_pictures/representations_vgg_face.pkl')

print(df)
#image_name = 'image0.jpg'
#feature_vector = data(image_name[0])
