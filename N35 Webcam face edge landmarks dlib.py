import cv2 as cv
import dlib 
import imutils
import numpy as np
from imutils import face_utils

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("/home/mohsencactus/Opencv/digit/opencv7_material/shape_predictor_68_face_landmarks.dat")

webcam = cv.VideoCapture(0)


counter = 0
minea = 0.3
while True:
    frame = webcam.read()[1]
    blank = np.zeros_like(frame)
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    rects = detector(gray,1)

    for rect in rects:
        shape = predictor(gray,rect)
        shape = face_utils.shape_to_np(shape)
        
        eye = shape[0:27]
        for (x,y) in eye:
            cv.circle(frame,(x,y),3,(255,0,0),-1)
            #cv.line(line_img,(xl1,yl1),(xl2,yl2),(255,0,0),10)

    
    cv.imshow("blank",blank)
    cv.imshow("frame",frame)
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break
    