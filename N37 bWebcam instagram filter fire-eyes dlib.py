import cv2 as cv
import dlib 
import numpy as np
from imutils import face_utils
import math

#####################################################
def distance(p1,p2):
    (x1,y1) = p1
    (x2,y2) = p2
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
    return dist  

#####################################################
def channel(img):
    _,_,channels = img.shape
    if channels < 4:
        new_img = cv.cvtColor(img, cv.COLOR_BGR2BGRA)
        return new_img
    else:
        return img

def masker(frame,img,roi,width,height):
    img = cv.resize(img,(width,height))
    imggray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    binar = cv.threshold(imggray, 25, 255, cv.THRESH_BINARY_INV)[1]
    roiwith = cv.bitwise_and(roi, roi, mask=binar)
    #fillednose = cv.bitwise_and(img,img,mask=binar)
    roiwith = channel(roiwith)
    filled = cv.add(roiwith, img)
    return filled

#####################################################
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("/home/mohsencactus/Opencv/digit/opencv7_material/shape_predictor_68_face_landmarks.dat")
webcam = cv.VideoCapture(0)
img = cv.imread("/home/mohsencactus/Desktop/trzcacak.rs-emoji-fire-png-49449.png",cv.IMREAD_UNCHANGED)
img = channel(img)
print(img.shape)
a = 10
b = 22
#####################################################
while True:
    frame = webcam.read()[1]
    frame = channel(frame)
    blank = np.zeros_like(frame)
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

#####################################################
    faces = detector(gray,1)    
    for face in faces:
        fpoints = predictor(gray,face)
        fpoints = face_utils.shape_to_np(fpoints)
        #for (x,y) in fpoints:
        #    cv.circle(frame,(x,y),3,(255,0,0),-1)

#####################################################
        reye = fpoints[36:42]
        leye = fpoints[42:48]
        rheight = int(distance(reye[5],reye[1]))+(b*2)
        rwidth = int(distance(reye[0],reye[3]))+(a*2)
        lheight = int(distance(leye[5],leye[1]))+(b*2)
        lwidth = int(distance(leye[0],leye[3]))+(a*2)
        #for (x,y) in reye:
        #    cv.circle(frame,(x,y),3,(255,255,0),-1)

#####################################################



#####################################################
        try:
            reyeroi = frame[reye[1][1]-b:reye[5][1]+b,reye[0][0]-a:reye[3][0]+a]
            cv.imshow("frame1",reyeroi)
            reyefilled = masker(frame,img,reyeroi,rwidth,rheight)
            frame[reye[1][1]-b:reye[5][1]+b,reye[0][0]-a:reye[3][0]+a] = reyefilled
################
            leyeroi = frame[leye[1][1]-b:leye[5][1]+b,leye[0][0]-a:leye[3][0]+a]
            cv.imshow("frame2",leyeroi)
            leyefilled = masker(frame,img,leyeroi,lwidth,lheight)
            frame[leye[1][1]-b:leye[5][1]+b,leye[0][0]-a:leye[3][0]+a] = leyefilled
################
        except Exception as ERR:
            print("ERRRR:",ERR)

#####################################################
    cv.imshow("frame",frame)
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break
    