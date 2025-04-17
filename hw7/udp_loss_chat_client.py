from socket import *

port = 3333
BUFF_SIZE = 1024
addr = ('localhost', port)

sock = socket(AF_INET, SOCK_DGRAM)
print("🟢 UDP Chat Client Ready")

try:
    while True:
        msg = input("-> ")
        reTx = 0

        while reTx < 5:
            resp = f"{reTx} {msg}"
            sock.sendto(resp.encode(), addr)
            sock.settimeout(2)

            try:
                data, _ = sock.recvfrom(BUFF_SIZE)
            except timeout:
                reTx += 1
                continue
            else:
                if data.decode() == 'ack':
                    break
        else:
            print("❌ 5회 재전송 실패. 메시지 전송 포기")
            continue

        # 서버의 응답 수신 및 출력
        sock.settimeout(None)
        data, _ = sock.recvfrom(BUFF_SIZE)
        print(f"<- {data.decode()}")

except KeyboardInterrupt:
    print("\n🛑 클라이언트 종료됨")
    sock.close()
