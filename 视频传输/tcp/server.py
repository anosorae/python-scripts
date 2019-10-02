import pickle
import socket
import struct
import cv2

HOST = ''
PORT = 8001
# fps = 20
bufSize = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
print("server bind complete")
s.listen()
print("server now listening")
conn, addr = s.accept()
print("connected from: ", addr)

data = b''
payload_size = struct.calcsize("L")

# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, fps, (640, 480))

while True:
    try:
        # Retrieve message size
        while len(data) < payload_size:
            data += conn.recv(bufSize)

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("L", packed_msg_size)[0]

        # Retrieve all data based on message size
        while len(data) < msg_size:
            data += conn.recv(bufSize)

        frame_data = data[:msg_size]
        data = data[msg_size:]

        # Extract frame
        frame = pickle.loads(frame_data)

        imgdecode = cv2.imdecode(frame, 1)  # 解码
        print('recieved one frame from: ', addr)
        # Display
        cv2.imshow('frame', imgdecode)

        # out.write(imgdecode)
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("exit by key!")
        break
    if cv2.waitKey(1) == 27:
        break
# out.release()
cv2.destroyAllWindows()
conn.close()
s.close()
