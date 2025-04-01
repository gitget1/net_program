from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    msg = input('계산할 두 정수 두자리와 연산을 넣으십시오: ')
    s.send(msg.encode())
    if msg == 'q':
        break
    data = s.recv(1024)
    print('결과:', data.decode())

s.close()
