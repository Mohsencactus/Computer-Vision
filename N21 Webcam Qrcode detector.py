import pyzbar.pyzbar as pyz
import cv2 as cv  

def firstletter(data,list = []):
    n = len(list)
    if (n == 0) or (n > 0 and list[n-1] != data):
        list.append(data)
    else:
        pass
    return list

webcam = cv.VideoCapture(0)

while True:
    _,frame = webcam.read()
    QRs = pyz.decode(frame)
######################################
    for QR in range (0,len(QRs)):
        cords = QRs[QR].rect
        x,y,w,h = cords
        if x < 0:
            x = -x
        if y < 0:
            y = -y
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
######################################
        a = firstletter(QRs[QR].data)
        print(a)
    cv.imshow("window",frame)
    key = cv.waitKey(1)
    if ord("q")==key:
        break
        cv.destroyAllWindows() 