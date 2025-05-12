import socket
import threading

def handler(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print('Received message:', data.decode())
        except:
            break
    sock.close()

def main():
    svr_addr = ('localhost', 2500)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(svr_addr)
    my_id = input('ID를 입력하세요: ')
    sock.send(('['+my_id+']').encode())
    th = threading.Thread(target=handler, args=(sock,))
    th.daemon = True
    th.start()
    while True:
        try:
            msg = '[' + my_id + '] ' + input('Message to send: ')
            sock.send(msg.encode())
            if 'quit' in msg:
                break
        except:
            break
    sock.close()

if __name__ == '__main__':
    main()