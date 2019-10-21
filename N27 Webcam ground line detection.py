import cv2 as cv
import numpy as np 
import math

video = cv.VideoCapture(1)

while True:
    avg2 = []
    avgline = []
    _,frame = video.read()
    yframe = len(frame)
    xframe = len(frame[1])
    roibinaried = np.zeros_like(frame)
    line_img = np.zeros_like(frame)
    roix1 = 0
    roiy1 = 0#int(yframe)
    roix2 = int(xframe)
    roiy2 = 0#int(yframe)
    roix3 = int(xframe)
    roiy3 = int(yframe*3/4)
    roix4 = 0
    roiy4 = int(yframe*3/4)
    roi = np.array([[(roix1,roiy1),(roix2,roiy2),(roix3,roiy3),(roix4,roiy4)]])
###################################
    gray = cv.cvtColor(frame,cv.COLOR_RGB2GRAY)
    blur = cv.GaussianBlur(gray,(5,5),0)
    canny = cv.Canny(blur,50,150)
    cannyrgb = cv.cvtColor(canny,cv.COLOR_GRAY2BGR)
    cv.fillPoly(roibinaried,roi,(255,255,255))
    filtered = cv.bitwise_and(cannyrgb,roibinaried) 
    cannyf = cv.Canny(filtered,50,150)
    lines = cv.HoughLinesP(cannyf,2,np.pi/180,100,np.array([]),minLineLength=5,maxLineGap=5) 
###################################
    try:
        if len(lines) > 0:
            for line in lines:
                xl1,yl1,xl2,yl2 = line[0]
                parameter = np.polyfit((xl1,xl2),(yl1,yl2),1)
                mslope = parameter[0]
                intercept = parameter[1]
                if mslope > 0.2 or mslope < -0.2 or mslope == 0:
                    avgline.append((mslope,intercept)) 
                    avg2.append((yl1,yl2))
###################################
            fitavg = np.average(avgline,axis=0)
            fitavg2 = np.average(avg2,axis=0)
            print(fitavg2)
        cv.line(frame,(0,int(fitavg2[0]+(yframe/6))),(xframe,int(fitavg2[1]+(yframe/6))),(255,0,0),10)
        highlight = cv.addWeighted(frame,0.8,line_img,1,1)
###################################
        cv.imshow('frame3',highlight)
    except Exception as error:
        print(error)
    key = cv.waitKey(1)
    if key == ord("q"):
        cv.destroyAllWindows()
        break