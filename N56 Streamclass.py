import cv2 as cv
import socket as skt
import pickle
import struct

class socket():
    def __init__(self):
        self.sock = skt.socket(skt.AF_INET,skt.SOCK_STREAM)

    def Client(self,IP='192.168.1.13',PORT=8089,camera=0):
        print("Connecting... ")
        self.sock.connect((IP,PORT))
        print("Connected ")
        self.webcam = cv.VideoCapture(camera)

    def Stream(self):
        self.frame = self.webcam.read()[1]
        self.frame = cv.resize(self.frame, (0,0), fx=0.5, fy=0.5) 
        self.data = pickle.dumps(self.frame)
        self.message_size = struct.pack("L", len(self.data))
        self.sock.sendall(self.message_size + self.data)

    def Server(self,IP='192.168.1.13',PORT=8089):
        print("Waiting for connection... ")
        self.sock.bind((IP,PORT))
        self.sock.listen(10)
        self.conn,self.addr = self.sock.accept()
        self.data = b""
        self.payload_size = struct.calcsize("L") 
        print("Connected ")

    def Receive(self):
        while len(self.data) < self.payload_size:
            self.data += self.conn.recv(4096)
        self.packed_msg_size = self.data[:self.payload_size]
        self.data = self.data[self.payload_size:]
        self.msg_size = struct.unpack("L", self.packed_msg_size)[0]
        while len(self.data) < self.msg_size:
            self.data += self.conn.recv(4096)
        self.frame_data = self.data[:self.msg_size]
        self.data = self.data[self.msg_size:]
        self.frame = pickle.loads(self.frame_data)
        return self.frame