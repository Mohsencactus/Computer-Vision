import pickle
import socket as sck
import struct
import cv2 as cv 

sock = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
sock.bind(('192.168.1.8', 8089))
sock.listen(1)
conn, addr = sock.accept()
print("Connected")

data = b""
payload_size = struct.calcsize("L") 

while True:
    while len(data) < payload_size:
        data += conn.recv(4096)

    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]

    while len(data) < msg_size:
        data += conn.recv(4096)

    frame_data = data[:msg_size]
    data = data[msg_size:]

    frame = pickle.loads(frame_data)

    cv.imshow('frame', frame)
    if ord("q") == cv.waitKey(1):
         cv.destroyAllWindows()
        break