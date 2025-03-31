import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())

name = 'MinSeong Kim'  
sock.send(name.encode())

student_id_bytes = sock.recv(4)
student_id = struct.unpack('>I', student_id_bytes)[0]  
print(f"{student_id}")

sock.close()
