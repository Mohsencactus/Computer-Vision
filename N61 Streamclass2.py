import socket as sck
import cv2 as cv
import pickle
import struct

class Socket:
	def __init__(self,camera=0):
		self.socket = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
		self.webcam = cv.VideoCapture(camera)
		self.data = b""
		self.payload_size = struct.calcsize("L")

	def Client(self,IP='192.168.1.8',PORT=8089):
		print("Connecting... ")
		self.socket.connect((IP,PORT))
		print("Connected ")

	def Server(self,IP='192.168.1.8',PORT=8089):
		print("Waiting for connection... ")
		self.socket.bind(('192.168.1.8', 8089))
		self.socket.listen()
		self.conn,self.addr = self.socket.accept()
		print("Connected ")

	def Clientsend(self,msg=''):
		self.socket.sendall(str.encode(str(msg)))
	
	def Clientreceive(self):
		self.rdata = self.socket.recv(1024)
		return self.rdata
	
	def Serverreceive(self):
		self.rdata = self.conn.recv(1024)
		return self.rdata

	def Serversend(self,msg=''):
		self.conn.sendall(str.encode(str(msg)))

	def ClientStream(self):
		self.frame = self.webcam.read()[1]
		self.frame = cv.resize(self.frame, (0,0), fx=0.5, fy=0.5)
		self.data = pickle.dumps(self.frame)
		self.message_size = struct.pack("L", len(self.data))
		self.socket.sendall(self.message_size + self.data)

	def ServerStream(self):
		self.frame = self.webcam.read()[1]
		self.frame = cv.resize(self.frame, (0,0), fx=0.5, fy=0.5)
		self.data = pickle.dumps(self.frame)
		self.message_size = struct.pack("L", len(self.data))
		self.conn.sendall(self.message_size + self.data)
	
	def ServerRStream(self):
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

	def ClientRStream(self):
	    while len(self.data) < self.payload_size:
	        self.data += self.socket.recv(4096)
	    self.packed_msg_size = self.data[:self.payload_size]
	    self.data = self.data[self.payload_size:]
	    self.msg_size = struct.unpack("L", self.packed_msg_size)[0]
	    while len(self.data) < self.msg_size:
	        self.data += self.socket.recv(4096)
	    self.frame_data = self.data[:self.msg_size]
	    self.data = self.data[self.msg_size:]
	    self.frame = pickle.loads(self.frame_data)
	    return self.frame

