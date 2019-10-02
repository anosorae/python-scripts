import socket
import pickle
import struct
import cv2

HOST = '127.0.0.1'
PORT = 8001

encode_param = [cv2.IMWRITE_JPEG_QUALITY, 20]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((HOST, PORT))
print("start to send frames...")

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    while not ret:
        ret, frame = cap.read()

    result, imgencode = cv2.imencode('.jpg', frame, encode_param)  # 编码

    data = pickle.dumps(imgencode)

    message_size = struct.pack("L", len(data))

    s.sendall(message_size)
    s.sendall(data)
    print("send one frame")

s.close()
