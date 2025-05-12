import socket
import threading
import time

clients = []  # 클라이언트 소켓 리스트

def handle_client(client_socket, addr):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            # 'quit'을 수신하면 해당 클라이언트를 목록에서 삭제
            if 'quit' in data.decode():
                if client_socket in clients:
                    print(addr, 'exited')
                    clients.remove(client_socket)
                break
            print(time.asctime() + str(addr) + ':' + data.decode())
            # 모든 클라이언트에게 전송
            for client in clients:
                if client != client_socket:
                    client.send(data)
        except:
            if client_socket in clients:
                clients.remove(client_socket)
            break
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 2500))
    server_socket.listen(5)
    print('Server Started')
    while True:
        client_socket, addr = server_socket.accept()
        print('new client', addr)
        clients.append(client_socket)
        th = threading.Thread(target=handle_client, args=(client_socket, addr))
        th.daemon = True
        th.start()

if __name__ == '__main__':
    main()