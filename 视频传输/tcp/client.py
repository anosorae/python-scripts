import cv2
import socket
import pickle
import struct

HOST = '192.168.1.107'
PORT = 8001
encode_param = [cv2.IMWRITE_JPEG_QUALITY, 20]  # 设置编码参数

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # 设置分辨率
cap.set(4, 480)

while True:
    ret, frame = cap.read()

    result, imgencode = cv2.imencode('.jpg', frame, encode_param)  # 编码

    # Serialize frame
    data = pickle.dumps(imgencode)
    # Send message length first
    message_size = struct.pack("L", len(data))
    # Then data
    s.sendall(message_size + data)
s.close()
