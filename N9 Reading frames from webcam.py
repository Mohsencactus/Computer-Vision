import cv2 as cv 

webcam = cv.VideoCapture(0)

while True: 
    _,frame = webcam.read()

    cv.imshow("frame",frame)
    key = cv.waitKey(1)
    if key == ord("q"):
        cv.destroyAllWindows()
        break