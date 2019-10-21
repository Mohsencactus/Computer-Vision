import Streamclass2 as SC

client = SC.Socket()
client.Client(IP='192.168.1.8')

while True:
    client.ClientStream()
    data = client.Clientreceive()
    print(data)
