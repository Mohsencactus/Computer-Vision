import cv2 as cv
import dlib 
import imutils
import numpy as np
from imutils import face_utils
import math  

def distance(x1,y1,x2,y2):  
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
    return dist  

def eyear(eye):
    d1 = distance(eye[1][0],eye[1][1],eye[5][0],eye[5][1])
    d2 = distance(eye[2][0],eye[2][1],eye[4][0],eye[4][1])
    d3 = distance(eye[0][0],eye[0][1],eye[3][0],eye[3][1])
    ear = (d1 + d2)/d3
    return ear

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("/home/mohsencactus/Opencv/digit/opencv7_material/shape_predictor_68_face_landmarks.dat")

webcam = cv.VideoCapture(0)

counter = 0
minear = 0.45

while True:
    frame = webcam.read()[1]
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    rects = detector(gray,1)

    for rect in rects:
        shape = predictor(gray,rect)
        shape = face_utils.shape_to_np(shape)
        
        reye = shape[36:42]
        leye = shape[42:48]
        eye = shape[36:48]
        
        reyeconv = cv.convexHull(reye)
        leyeconv = cv.convexHull(leye)        
        cv.drawContours(frame, [reyeconv], -1, (255,0,0), 1)
        cv.drawContours(frame, [leyeconv], -1, (255,0,0), 1)

        for (x,y) in eye:
            cv.circle(frame,(x,y),2,(255,255,0),-1)

        (x,y) = leye[0]
        cv.circle(frame,(x,y),2,(255,0,255),-1)

        rear = eyear(reye)
        lear = eyear(leye)
        ear = (rear+lear)/2
        ear = int(ear*100)/100

        if ear < minear:
            counter = counter + 1
        cv.putText(frame,'EAR is: ' +str(ear),(0,80),cv.FONT_HERSHEY_DUPLEX,1.0,(255, 255, 0), 1)
        cv.putText(frame,'Counter is: ' +str(counter),(0,40),cv.FONT_HERSHEY_DUPLEX,1.0,(255, 0, 0), 1)
        
    cv.imshow("frame",frame)
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break
    