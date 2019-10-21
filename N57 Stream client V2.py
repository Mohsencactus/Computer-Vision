import Streamclass as SC

client = SC.socket()

client.Client(IP='192.168.1.8', PORT=8089, camera=0)

while True:
	client.Stream()