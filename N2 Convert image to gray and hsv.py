import cv2 as cv 

cv.namedWindow("window1",cv.WINDOW_NORMAL)
cv.namedWindow("window2",cv.WINDOW_NORMAL)
cv.namedWindow("window3",cv.WINDOW_NORMAL)
cv.namedWindow("window4",cv.WINDOW_NORMAL)

impath = ("/home/mohsencactus/python 2/Begin/2skele.jpg")
image = cv.imread(impath)

hsv_img = cv.cvtColor(image,cv.COLOR_BGR2HSV)
gray_img = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
bgr_img = cv.cvtColor(image,cv.COLOR_BGR2RGB)

/home/mohsencactus/files/Codes/Github Python/Python Opencv-start/haar.py
cv.imshow("window1",image)
cv.imshow("window2",gray_img)
cv.imshow("window3",hsv_img)
cv.imshow("window4",bgr_img)
cv.waitKey(0)

