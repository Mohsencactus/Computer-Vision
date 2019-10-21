import cv2 as cv
import socket as skt
import pickle
import struct

sock = skt.socket(skt.AF_INET,skt.SOCK_STREAM)

webcam = cv.VideoCapture(0)
sock.connect(('192.168.1.8',8089))

while True:
    _,frame = webcam.read()
    frame = cv.resize(frame, (0,0), fx=0.5, fy=0.5) 
    data = pickle.dumps(frame)
    message_size = struct.pack("L", len(data))
    sock.sendall(message_size + data)
