import cv2
import time
import numbp as np
fourcc=cv2.Videowriter(*"XVID")
outputfile=cv2.videowriter("output",fourcc,20.0,(640,480))
cap=cv2.VideoCapture(0)
time.sleep(2)
bg=0
for i in range(60):
    ret,bg=cap.read()
