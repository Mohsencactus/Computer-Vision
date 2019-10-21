import cv2 as cv
import numpy as np 
import math

def cords(slin,yframe,img):
    slope,inter = slin
    y1 = yframe
    y2 = int(yframe*(3/5))
    x1 = int((y1-inter)/slope)
    x2 = int((y2-inter)/slope)
    cv.line(img,(x1,y1),(x2,y2),(255,0,0),10)
    
video = cv.VideoCapture("/home/mohsencactus/Github Python/Python Opencv-start/road.mp4")

while True:
    _,frame = video.read()
    yframe = len(frame)
    xframe = len(frame[1])
    lane_tri = np.array([[(200,yframe),(1100,yframe),(550,250)]])

    gray = cv.cvtColor(frame,cv.COLOR_RGB2GRAY)
    blur = cv.GaussianBlur(gray,(5,5),0)
    canny = cv.Canny(blur,50,150)
    cannyrgb = cv.cvtColor(canny,cv.COLOR_GRAY2BGR)
    roibinaried = np.zeros_like(frame)
    cv.fillPoly(roibinaried,lane_tri,(255,255,255))

    filtered = cv.bitwise_and(cannyrgb,roibinaried) 
    cannyf = cv.Canny(filtered,50,150)

    lines = cv.HoughLinesP(cannyf,2,np.pi/180,100,np.array([]),minLineLength=5,maxLineGap=5)

   line_img = np.zeros_like(frame)
    left_fit = []
    right_fit = [] 
    if len(lines) > 0:
        for line in lines:
            xl1,yl1,xl2,yl2 = line[0]
            #cv.line(line_img,(xl1,yl1),(xl2,yl2),(255,0,0),10)
            parameter = np.polyfit((xl1,xl2),(yl1,yl2),1)
            slope = parameter[0]
            intercept = parameter[1]
            if slope < 0:
                left_fit.append((slope,intercept))
            else :
                right_fit.append((slope,intercept))
        left_fitavg = np.average(left_fit,axis=0)
        right_fitavg = np.average(right_fit,axis=0)
        average = [left_fitavg,right_fitavg]
        for i in range (0,len(average)):
            if isinstance(average[i], np.ndarray) == True:
                cords(average[i],yframe,line_img)

    highlight = cv.addWeighted(frame,0.8,line_img,1,1)

    cv.imshow('frame1',highlight)

    key = cv.waitKey(1)
    if key == ord("q"):
        break
        cv.destroyAllWindows()
