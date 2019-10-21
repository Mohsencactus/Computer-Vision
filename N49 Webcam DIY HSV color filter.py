import cv2 as cv
import numpy as np 

webcam = cv.VideoCapture(0)
#webcam.set(3, 10)
#webcam.set(4, 10)
p = 0

cv.namedWindow("frame",cv.WINDOW_NORMAL)
cv.namedWindow("frame2",cv.WINDOW_NORMAL)
while True:
    _,frame = webcam.read()
    hsv = cv.cvtColor(frame,cv.COLOR_RGB2HSV)
    img = np.zeros_like(frame)

    for i in range(0,hsv.shape[0]):
        for j in range(0,hsv.shape[1]):
            arr = hsv[i,j]
            arr2 = frame[i,j]
            arr3 = img[i,j]
            if arr[1] != 0 or arr[2] >= 40: 
                continue
            else:
                arr3[0]=255
                arr3[1]=0
                arr3[2]=255
                arr2[0]=255
                arr2[1]=0
                arr2[2]=255

    cv.imshow("frame",frame)
    cv.imshow("frame2",img)
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break
