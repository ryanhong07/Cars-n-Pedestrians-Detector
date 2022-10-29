import cv2
from random import randrange

video = cv2.VideoCapture('Dashcam4.mp4')

car_tracker = cv2.CascadeClassifier('cars2.xml')
pedestrian_tracker = cv2.CascadeClassifier('haarcascade_fullbody.xml')

while True:
    
    (read_successful, frame) = video.read()
    
    if read_successful:
        grayscaled_frame = cv2.cvtColor(frame,  cv2.COLOR_BGR2GRAY)
    else:
        break
    
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frame)
    
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        
    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow('Clever Programmer Car Detector', frame)
    
    key = cv2.waitKey(1)
    if key==81 or key==113:
        break

print("Code Completed") 