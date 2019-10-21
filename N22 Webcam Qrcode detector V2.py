import pyzbar.pyzbar as pyz
import cv2 as cv 
import numpy as np 
from copy import deepcopy

def Listwithoutrepeat(data,list = []):
    n = len(list)
    if (n == 0) or (n > 0 and list[n-1] != data):
        list.append(data)
    else:
        pass
    return list

webcam = cv.VideoCapture(0)

while True:
    _,frame = webcam.read()   
    black = np.zeros_like(frame)
    QRs = pyz.decode(frame)
    for QR in range (0,len(QRs)):
##################################################
        cords = QRs[QR].rect
        x,y,w,h = cords
        if x < 0:
            x = -x
        if y < 0:
            y = -y
        pointls = [0,0,0,0]
        polygon = QRs[QR].polygon
        for i in range (0,4):
            points = polygon[i]
            pointx = points[0]
            pointy = points[1]
            pointls[i] = (pointx,pointy)
            cv.circle(frame,(int(pointx),int(pointy)),4,(255,0,255),2)
##################################################
        QRframe = np.array([[pointls[0],pointls[1],pointls[2],pointls[3]]])
        cv.fillPoly(black,QRframe,(255,255,255))
        filtered = cv.bitwise_and(frame,black)
        frame = cv.addWeighted(frame,0.8,filtered,1,1)
##################################################
        name = str(deepcopy(QRs[QR].data))
        name = name.replace('b','', 1)
        name = name.replace("'",'')
        name = name.replace('"','')
        name = name.replace("http://",'')
        name2 = name.split(',')
##################################################        
        allqrs = Listwithoutrepeat(name2)
        rect = QRs[QR].rect
        center = (int(rect.left+(rect.width/2)),int(rect.top+(rect.height/2)))
        cv.circle(frame,center,3,(0,255,255),3)
        print(QRs,center)
##################################################
    cv.imshow("window",frame)
    key = cv.waitKey(1)
    if ord("q")==key:
        break
        cv.destroyAllWindows() 