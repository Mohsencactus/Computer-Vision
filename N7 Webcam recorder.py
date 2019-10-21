import numpy as np
import cv2 as cv

webcam = cv.VideoCapture(0)
_,frame = webcam.read()

yframe = len(frame)
xframe = len(frame[0])

fourcc = cv.VideoWriter_fourcc(*'XVID')
videorec = cv.VideoWriter('Record1.mp4',fourcc,20,(xframe,yframe))

while True:
    _,frame = webcam.read()
    videorec.write(frame)

    cv.imshow("window",frame)
    key = cv.waitKey(1)
    if key == ord("q"):
        cv.destroyAllWindows()
        break
