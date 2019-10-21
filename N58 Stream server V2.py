import cv2 as cv
import Streamclass as SC

server = SC.socket()

server.Server(IP='192.168.1.8', PORT=8089)

while True:
	frame = server.Receive()

	cv.imshow("frame",frame)
	if ord("q") == cv.waitKey(1):
		cv.destroyAllWindows()
		break