import socket
import random

HOST = '127.0.0.1'
PORT = 9002

s = socket.socket()
s.bind((HOST, PORT))
s.listen(1)
print("Device2 실행 중 (심박수/걸음수/칼로리)...")

conn, addr = s.accept()
print(f"연결됨: {addr}")

while True:
    msg = conn.recv(1024).decode()
    if msg.lower() == 'quit':
        print("종료 요청 받음.")
        break
    elif msg.lower() == 'request':
        heart = random.randint(40, 140)
        steps = random.randint(2000, 6000)
        cal = random.randint(1000, 4000)
        data = f"{heart},{steps},{cal}"
        conn.send(data.encode())
    else:
        print("알 수 없는 명령:", msg)

conn.close()
s.close()
