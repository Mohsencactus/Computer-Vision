import cv2 as cv

webcam1 = cv.VideoCapture(0)
webcam2 = cv.VideoCapture(1)

while True:
    _,frame1 = webcam1.read()
    _,frame2 = webcam2.read()
        
    cv.imshow("frame1",frame1)
    cv.imshow("frame2",frame2)
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break