import cv2 as cv 
import numpy as np 

def nthn(X):
    pass

impath = ("/home/mohsencactus/python 2/Begin/2skele.jpg")
img = cv.imread(impath)
skelet = np.copy(img)
hsv = cv.cvtColor(skelet,cv.COLOR_BGR2HSV)

cv.namedWindow("window2",cv.WINDOW_NORMAL)

cv.createTrackbar("Hmin","window2",0,255,nthn)
cv.createTrackbar("Hmax","window2",0,180,nthn)
cv.createTrackbar("Smin","window2",0,255,nthn)
cv.createTrackbar("Smax","window2",0,255,nthn)
cv.createTrackbar("Vmin","window2",0,255,nthn)
cv.createTrackbar("Vmax","window2",0,255,nthn)
cv.setTrackbarPos("Hmax","window2",180)
cv.setTrackbarPos("Smax","window2",255)
cv.setTrackbarPos("Vmax","window2",255)

while True:
    Hmin = cv.getTrackbarPos("Hmin","window2")
    Smin = cv.getTrackbarPos("Smin","window2")
    Vmin = cv.getTrackbarPos("Vmin","window2")
    Hmax = cv.getTrackbarPos("Hmax","window2")
    Smax = cv.getTrackbarPos("Smax","window2")
    Vmax = cv.getTrackbarPos("Vmax","window2")

    mins = np.array([Hmin,Smin,Vmin])
    maxs = np.array([Hmax,Smax,Vmax])
    binaried = cv.inRange(hsv,mins,maxs)
    filtered = cv.bitwise_and(skelet,skelet,mask = binaried)

    cv.imshow("window2",filtered)
    key = cv.waitKey(1)
    if key == ord("q"):
        cv.destroyAllWindows()
        break
