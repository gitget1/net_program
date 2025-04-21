import socket

# 메일박스 저장소 (mboxID 별 메시지 큐)
mailboxes = {}

# 서버 소켓 설정
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 9999))
print("📬 UDP Message Server is running on port 9999...")

while True:
    data, addr = server_socket.recvfrom(1024)
    message = data.decode().strip()

    if message.startswith("send "):
        parts = message.split(' ', 2)
        if len(parts) < 3:
            server_socket.sendto("Invalid send format".encode(), addr)
            continue

        mbox_id = parts[1]
        msg_content = parts[2]

        if mbox_id not in mailboxes:
            mailboxes[mbox_id] = []

        mailboxes[mbox_id].append(msg_content)
        server_socket.sendto("OK".encode(), addr)

    elif message.startswith("receive "):
        parts = message.split(' ', 1)
        if len(parts) < 2:
            server_socket.sendto("Invalid receive format".encode(), addr)
            continue

        mbox_id = parts[1]

        if mbox_id in mailboxes and mailboxes[mbox_id]:
            next_msg = mailboxes[mbox_id].pop(0)
            server_socket.sendto(next_msg.encode(), addr)
        else:
            server_socket.sendto("No messages".encode(), addr)

    elif message == "quit":
        print("🔚 Quit signal received. Shutting down.")
        break

    else:
        server_socket.sendto("Unknown command".encode(), addr)

server_socket.close()
