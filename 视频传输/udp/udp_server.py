import socket
import pickle
import cv2
import struct

HOST = ''
PORT = 8001

bufSize = 65535

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
print("server now bind at port: ", PORT)

data = b''
payload_size = struct.calcsize("L")

while True:
    data, addr = s.recvfrom(bufSize)
    if len(data) != payload_size:
        continue

    length = struct.unpack("L", data)[0]

    data, addr = s.recvfrom(bufSize)
    if length != len(data):
        continue

    frame_codes = pickle.loads(data)
    image = cv2.imdecode(frame_codes, 1)
    print("recieved frame+")
    cv2.imshow("pi_cam", image)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
s.close()
