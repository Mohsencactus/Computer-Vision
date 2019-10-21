import numpy as np
import cv2 as cv

webcam = cv.VideoCapture(0)
window = ['wcp1','wcp2','wcp3','wcp4','wcp5','wcp6','wcp7']

while(True):
    cntur = [0,0,0,0,0,0,0]
    _,frame = webcam.read()

    grayed = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    grayblured = cv.GaussianBlur(grayed, (5, 5), 0)
    binaried = cv.inRange(grayblured, 0, 90)
    #medianed = cv.medianBlur(binaried, 25)
    contours,hiarchy = cv.findContours(binaried,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
   
    if len(contours) > 0:
            cnt = max(contours, key = cv.contourArea)
            x,y,w,h = cv.boundingRect(cnt)
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            target = binaried[y:y+h,x:x+w]
            xtarget = len(target[0])
            ytarget = len(target)
            cv.imshow("frame6", target)

            nc1 = target[0:0,0:xtarget]
            nc2 = target[int(ytarget/4):int((3*ytarget)/8),int((xtarget*5)/6):xtarget]
            nc3 = target[int((ytarget*6)/8):int((ytarget*7)/8),int((xtarget*5)/6):xtarget]
            nc4 = target[int((ytarget*7)/8):ytarget,int(xtarget/3):int((xtarget*2)/3)] 
            nc5 = target[int((6*ytarget)/8):int((ytarget*5)/6),0:int(xtarget/6)] 
            nc6 = target[int(ytarget/4):int((3*ytarget)/8),0:int(xtarget/6)] 
            nc7 = target[int(ytarget/2):int((5*ytarget)/8),0:xtarget]
            numc = [nc1,nc2,nc3,nc4,nc5,nc6,nc7]
            for o in range(0,7):
                cv.imshow(window[o],numc[o])
                contoursn = cv.findContours(numc[o],cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)[1]
                cntur[o] = cntur[o]+len(contoursn)
            if (cntur == [1,1,1,1,1,1,0]):
                adad = 0
            elif (cntur == [0,1,1,0,0,0,0]):
                adad = 1
            elif (cntur == [1,1,0,1,1,0,1]):
                adad = 2
            elif (cntur == [1,1,1,1,0,0,1]):
                adad = 3
            elif (cntur == [0,1,1,0,0,1,1]):
                adad = 4
            elif (cntur == [1,0,1,1,0,1,1]):
                adad = 5
            elif (cntur == [1,1,1,1,1,0,1]):
                adad = 6
            elif (cntur == [1,1,1,0,0,0,0]):
                adad = 7
            elif (cntur == [1,1,1,1,1,1,1]):
                adad = 8
            elif (cntur == [1,1,0,1,1,1,1]):
                adad = 9
            else :
                adad = 'not found'
            print(cntur)
            print(adad)
###################
    cv.imshow("frame1", frame)
    #cv.imshow("frame6", grayed)
    #cv.imshow("frame3", binaried)
    #cv.imshow("frame4", medianed)
    #cv.imshow("frame5", filtered)
###################################
    ikey = cv.waitKey(1)
    if(ord("q") == ikey):
        break
cv.destroyAllWindows()
 

