import cv2 as cv
import numpy as np
from time import sleep
#######################################
cv.namedWindow("window",cv.WINDOW_NORMAL)
#######################################
webcam = cv.VideoCapture(0)
for i in range(10):
    _,background = webcam.read()
    sleep(0.1)
#######################################
hsvmin = np.array([100,85,15])
hsvmax = np.array([120,255,255])
#######################################
while True:
    _,frame = webcam.read()
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    binaried = cv.inRange(hsv,hsvmin,hsvmax)
#######################################
    cloak = cv.morphologyEx(binaried, cv.MORPH_OPEN, np.ones((3,3),np.uint8),iterations=2)
    cloakrevers = cv.bitwise_not(cloak)
#######################################  
    backgoncloak = cv.bitwise_and(background,background,mask=cloak)
    cloakonframe = cv.bitwise_and(frame,frame,mask=cloakrevers)
    final = cv.addWeighted(backgoncloak,1,cloakonframe,1,0)
#######################################
    cv.imshow("window",final)
    key = cv.waitKey(1)
    if key == ord("q"):
        cv.destroyAllWindows()
        break