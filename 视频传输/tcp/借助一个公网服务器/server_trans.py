import socket

HOST = ''
PORT = 8001
bufSize = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST, PORT))
print('Socket bind complete')
s.listen(2)
print('Socket now listening')

conn_src, addr_src = s.accept()
print('source connected from: ', addr_src)

conn_dst, addr_dst = s.accept()
print('destination connected from: ', addr_dst)


while True:
    data = conn_src.recv(bufSize)
    conn_dst.sendall(data)

conn_src.close()
conn_dst.close()
s.close()
