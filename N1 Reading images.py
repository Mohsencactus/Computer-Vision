import cv2 as cv 


cv.namedWindow("window1",cv.WINDOW_NORMAL)

impath = ("/home/mohsencactus/python 2/Begin/2skele.jpg")
img = cv.imread(impath)


cv.imshow("window1",img)
cv.waitKey(0)

