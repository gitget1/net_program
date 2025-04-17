from socket import *
import random

port = 3333
BUFF_SIZE = 1024
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))
print("🔵 UDP Chat Server Ready")

last_msg = None
server_reTx = 0  # 서버 메시지도 번호 붙이기 위해 사용

try:
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
        msg = data.decode()

        if random.random() <= 0.5:
            continue
        else:
            sock.sendto(b'ack', addr)

            if msg != last_msg:
                print(f"<- {msg}")
                last_msg = msg

            reply = input("-> ")
            reply_with_number = f"{server_reTx} {reply}"
            sock.sendto(reply_with_number.encode(), addr)
            server_reTx += 1

except KeyboardInterrupt:
    print("\n🛑 서버 종료됨")
    sock.close()
