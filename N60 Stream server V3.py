import Streamclass2 as SC
import cv2 as cv

server = SC.Socket()
server.Server(IP='192.168.1.8')

while True:
    frame = server.ServerRStream()
    server.Serversend(msg='HAHA')

    cv.imshow("frame",frame)
    if ord("q") == cv.waitKey(1):
    	cv.destroyAllWindows()
    	break
    