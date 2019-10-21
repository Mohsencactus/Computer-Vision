import cv2 as cv 

webcam = cv.VideoCapture(0)

while True: 
    _,frame = webcam.read()
    
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    bgr = cv.cvtColor(frame,cv.COLOR_BGR2RGB)

    cv.imshow("frame",frame)
    cv.imshow("gray",gray)
    cv.imshow("hsv",hsv)
    cv.imshow("bgr",bgr)
    key = cv.waitKey(1)
    if key == ord("q"):
        cv.destroyAllWindows()
        break