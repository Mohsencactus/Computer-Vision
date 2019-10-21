import numpy as np
import cv2 as cv

webcam = cv.VideoCapture(0)
###################################
window = ['wcp1','wcp2','wcp3','wcp4','wcp5','wcp6','wcp7']

while(True):
    cntur = [0,0,0,0,0,0,0]
    _,frame = webcam.read()

    grayed = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    grayblured = cv.GaussianBlur(grayed, (5, 5), 0)
    binaried = cv.inRange(grayblured, 0, 90)
    #medianed = cv.medianBlur(binaried, 25)
    contours,hiarchy = cv.findContours(binaried,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
   ################# contouring #######################
    if len(contours) > 0:
            cnt = max(contours, key = cv.contourArea)
            (x,y), radius = cv.minEnclosingCircle(cnt) 
            center = (int(x),int(y)) 
            cv.circle(frame,center,2,(255,0,0),2)
            x,y,w,h = cv.boundingRect(cnt)
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            number = binaried[y:y+h,x:x+w]
            xnum = len(number[0])
            ynum = len(number)
            mky = int(len(number)/2)
            mkx = int(len(number[0])/2)
            cv.imshow("frame6", number)

            #nc1 = number[0:int(ynum/8),0:xnum]
            #nc2 = number[int(ynum/4):int((3*ynum)/8),int((xnum*5)/6):xnum]
            #nc3 = number[int((ynum*6)/8):int((ynum*7)/8),int((xnum*5)/6):xnum]
            #nc4 = number[int((ynum*7)/8):ynum,int(xnum/3):int((xnum*2)/3)] 
            #nc5 = number[int((6*ynum)/8):int((ynum*5)/6),0:int(xnum/6)] 
            #nc6 = number[int(ynum/4):int((3*ynum)/8),0:int(xnum/6)] 
            #nc7 = number[int(ynum/2):int((5*ynum)/8),0:xnum]
            #numc = [nc1,nc2,nc3,nc4,nc5,nc6,nc7]
            #for o in range(0,7):
            #    #cv.imshow(window[d],numc[o])
            #    contoursn = cv.findContours(numc[o],cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)[1]
            #    cntur[o] = cntur[o]+len(contoursn)
            #if (cntur == [1,1,1,1,1,1,0]):
            #    adad = 0
            #elif (cntur == [0,1,1,0,0,0,0]):
            #    adad = 1
            #elif (cntur == [1,1,0,1,1,0,1]):
            #    adad = 2
            #elif (cntur == [1,1,1,1,0,0,1]):
            #    adad = 3
            #elif (cntur == [0,1,1,0,0,1,1]):
            #    adad = 4
            #elif (cntur == [1,0,1,1,0,1,1]):
            #    adad = 5
            #elif (cntur == [1,1,1,1,1,0,1]):
            #    adad = 6
            #elif (cntur == [1,1,1,0,0,0,0]):
            #    adad = 7
            #elif (cntur == [1,1,1,1,1,1,1]):
            #    adad = 8
            #elif (cntur == [1,1,0,1,1,1,1]):
            #    adad = 9
            #else :
            #    adad = 'not found'
            #print(cntur)
            #print(adad)
###################
    cv.imshow("frame1", frame)
    ikey = cv.waitKey(1)
    if(ord("q") == ikey):
        break
cv.destroyAllWindows()
 

