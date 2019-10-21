import cv2 as cv
import numpy as np 
def nothing(x):
    pass

webcam = cv.VideoCapture(0)
cv.namedWindow('frame')

cv.createTrackbar('hmin','frame',0,255,nothing)
cv.createTrackbar('hmax','frame',0,255,nothing)
cv.createTrackbar('smin','frame',0,255,nothing)
cv.createTrackbar('smax','frame',0,255,nothing)
cv.createTrackbar('vmin','frame',0,255,nothing)
cv.createTrackbar('vmax','frame',0,255,nothing)
cv.createTrackbar('blur','frame',0,4,nothing)
cv.setTrackbarPos('hmax','frame',255)
cv.setTrackbarPos('smax','frame',255)
cv.setTrackbarPos('vmax','frame',255)

while True:
    hmin = cv.getTrackbarPos('hmin','frame')
    hmax = cv.getTrackbarPos('hmax','frame')
    smin = cv.getTrackbarPos('smin','frame')
    smax = cv.getTrackbarPos('smax','frame')
    vmin = cv.getTrackbarPos('vmin','frame')
    vmax = cv.getTrackbarPos('vmax','frame')
    blur = cv.getTrackbarPos('blur','frame')
    hsvmin = np.array([hmin,smin,vmin])
    hsvmax = np.array([hmax,smax,vmax])


    _,frame = webcam.read()
    if (blur == 1):
        frame = cv.bilateralFilter(frame,9,75,75)
    elif (blur == 2):
        frame = cv.blur(frame,(5,5))
    elif (blur == 3):
        frame = cv.GaussianBlur(frame,(15,15),0)
    elif (blur == 4):
        frame = cv.medianBlur(frame,25)
    else :
        pass
    hsv = cv.cvtColor(frame,cv.COLOR_RGB2HSV)
    binaried = cv.inRange(hsv,hsvmin,hsvmax)
    filtered = cv.bitwise_and(frame,frame,mask = binaried)
    
    cv.imshow('frame',filtered)
    key = cv.waitKey(1)
    if key == ord("q"):
        break
        cv.destroyAllWindows