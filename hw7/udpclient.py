import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    user_input = input('Enter the message("send mboxId message" or "receive mboxId" or "quit"):')
    client_socket.sendto(user_input.encode(), ('localhost', 9999))

    if user_input == "quit":
        break

    data, _ = client_socket.recvfrom(1024)
    print(data.decode())

client_socket.close()
