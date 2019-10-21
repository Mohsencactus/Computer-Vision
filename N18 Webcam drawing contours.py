import cv2 as cv 
import numpy as np 

webcam = cv.VideoCapture(0)

hsvmin = np.array([100,160,0])
hsvmax = np.array([120,255,255])

while True: 
    _,frame = webcam.read()
    
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    binaried = cv.inRange(hsv,hsvmin,hsvmax)
    filtered = cv.bitwise_and(frame,frame,mask = binaried)

    contours = cv.findContours(binaried,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)[0]

    if len(contours) > 0:
        contour = max(contours, key = cv.contourArea)
        (xc,yc),radius = cv.minEnclosingCircle(contour)
        (x,y,w,h) = cv.boundingRect(contour) 
        
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        cv.circle(frame,(int(xc),int(yc)),int(radius),(255,0,255),2)
        cv.circle(frame,(int(xc),int(yc)),1,(255,0,255),2)

    else :
        print("Nothing found to contour")

    cv.imshow("frame",frame)
    key = cv.waitKey(1)
    if key == ord("q"):
        cv.destroyAllWindows()
        break