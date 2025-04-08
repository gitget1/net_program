import socket
import random

HOST = '127.0.0.1'
PORT = 9001

s = socket.socket()
s.bind((HOST, PORT))
s.listen(1)
print("Device1 실행 중 (온도/습도/조도)...")

conn, addr = s.accept()
print(f"연결됨: {addr}")

while True:
    msg = conn.recv(1024).decode()
    if msg.lower() == 'quit':
        print("종료 요청 받음.")
        break
    elif msg.lower() == 'request':
        temp = random.randint(0, 40)
        humid = random.randint(0, 100)
        illum = random.randint(70, 150)
        data = f"{temp},{humid},{illum}"
        conn.send(data.encode())
    else:
        print("알 수 없는 명령:", msg)

conn.close()
s.close()
