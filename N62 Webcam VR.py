import cv2 as cv 

webcam = cv.VideoCapture(0)

cv.namedWindow("window",cv.WINDOW_FREERATIO)
cv.namedWindow("window2",cv.WINDOW_FREERATIO)
while True:
    _,frame = webcam.read()

    cv.imshow("window",frame)
    cv.imshow("window2",frame)
##############################################
    if ord("q") == cv.waitKey(1):
        cv.destroyAllWindows()
        break