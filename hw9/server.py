import socket
import select
import time

BUFFER = 1024
PORT = 2500

s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s_sock.bind(('', PORT))
s_sock.listen(5)

socks = [s_sock]  # 소켓 리스트에 서버 소켓 추가

print(str(PORT) + '에서 접속 대기 중')

while True:
    # 읽기 이벤트(연결요청 및 데이터수신) 대기
    r_sock, _, _ = select.select(socks, [], [])
    for s in r_sock:
        if s == s_sock:
            # 새로운 클라이언트의 연결 요청 이벤트 발생
            c_sock, addr = s_sock.accept()
            socks.append(c_sock)
            print('Client ({}) connected'.format(addr))
        else:
            # 기존 클라이언트의 데이터 수신 이벤트 발생
            try:
                data = s.recv(BUFFER)
                if not data:
                    s.close()
                    socks.remove(s)
                    continue
                print(time.asctime() + ' Received:', data.decode())
                # 모든 클라이언트에게 메시지 전송
                for client in socks:
                    if client != s_sock and client != s:
                        client.send(data)
            except:
                s.close()
                socks.remove(s)