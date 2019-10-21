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
    img = np.zeros_like(frame)

    for i in range(0,frame.shape[0]):
        for j in range(0,frame.shape[1]):
            arr = frame[i,j]
            arr2 = img[i,j]
            if arr[0] > 250 and arr[1] > 250 and arr[2] > 250:
                break
            if ((arr[1]+p) >= arr[0] and (arr[1]-p) <= arr[0]) and ((arr[1]+p) >= arr[2] and (arr[1]-p) <= arr[2]):
                arr2[0]=255
                arr2[1]=0
                arr2[2]=255
                arr[0]=255
                arr[1]=0
                arr[2]=255
            else:
                print("bye")

    cv.imshow("frame",frame)
    cv.imshow("frame2",img)
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break
