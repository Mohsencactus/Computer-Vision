import cv2 as cv 
import numpy as np 

def nthn(X):
    pass

impath = ("/home/mohsencactus/python 2/Begin/2skele.jpg")
img = cv.imread(impath)

cv.namedWindow("window2",cv.WINDOW_NORMAL)

cv.createTrackbar("Hmin","window2",0,255,nthn)
cv.createTrackbar("Hmax","window2",0,180,nthn)
cv.createTrackbar("Smin","window2",0,255,nthn)
cv.createTrackbar("Smax","window2",0,255,nthn)
cv.createTrackbar("Vmin","window2",0,255,nthn)
cv.createTrackbar("Vmax","window2",0,255,nthn)
cv.createTrackbar('Blur','window2',0,4,nthn)
cv.setTrackbarPos("Hmax","window2",180)
cv.setTrackbarPos("Smax","window2",255)
cv.setTrackbarPos("Vmax","window2",255)

while True:
    skelet = np.copy(img)

    Hmin = cv.getTrackbarPos("Hmin","window2")
    Smin = cv.getTrackbarPos("Smin","window2")
    Vmin = cv.getTrackbarPos("Vmin","window2")
    Hmax = cv.getTrackbarPos("Hmax","window2")
    Smax = cv.getTrackbarPos("Smax","window2")
    Vmax = cv.getTrackbarPos("Vmax","window2")
    Blur = cv.getTrackbarPos('Blur','window2')

    mins = np.array([Hmin,Smin,Vmin])
    maxs = np.array([Hmax,Smax,Vmax])
    
    if (Blur == 1):
        skelet = cv.bilateralFilter(skelet,9,75,75)
    elif (Blur == 2):
        skelet = cv.blur(skelet,(5,5))
    elif (Blur == 3):
        skelet = cv.GaussianBlur(skelet,(15,15),0)
    elif (Blur == 4):
        skelet = cv.medianBlur(skelet,25)
    else :
        pass
    hsv = cv.cvtColor(skelet,cv.COLOR_BGR2HSV)
    binaried = cv.inRange(hsv,mins,maxs)
    filtered = cv.bitwise_and(skelet,skelet,mask = binaried)

    cv.imshow("window2",filtered)
    key = cv.waitKey(1)
    if key == ord("q"):
        cv.destroyAllWindows()
        break




