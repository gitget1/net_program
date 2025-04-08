from socket import *
import os


s = socket()
s.bind(('', 80))
s.listen(10)
print("웹서버 실행 중")

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    if not data:
        c.close()
        continue

    msg = data.decode(errors='ignore')
    req = msg.split('\r\n')
    if len(req) < 1:
        c.close()
        continue

    request_line = req[0]
    print("요청 라인:", request_line)


    tokens = request_line.split()
    if len(tokens) < 2 or tokens[0] != 'GET':
        c.close()
        continue

    path = tokens[1]  # ex: /index.html
    filename = path.lstrip('/')  # ex: index.html

 
    try:
        if filename == '':
            filename = 'index.html'

        if filename == 'index.html':
            f = open(filename, 'r', encoding='utf-8')
            mimeType = 'text/html'
            data = f.read()
            f.close()

            c.send(b'HTTP/1.1 200 OK\r\n')
            c.send(('Content-Type: ' + mimeType + '\r\n').encode())
            c.send(b'\r\n')
            c.send(data.encode('euc-kr')) 

        elif filename == 'iot-1.png':
            f = open(filename, 'rb')
            mimeType = 'image/png'
            data = f.read()
            f.close()

            c.send(b'HTTP/1.1 200 OK\r\n')
            c.send(('Content-Type: ' + mimeType + '\r\n').encode())
            c.send(b'\r\n')
            c.send(data)

        elif filename == 'favicon.ico':
            f = open(filename, 'rb')
            mimeType = 'image/x-icon'
            data = f.read()
            f.close()

            c.send(b'HTTP/1.1 200 OK\r\n')
            c.send(('Content-Type: ' + mimeType + '\r\n').encode())
            c.send(b'\r\n')
            c.send(data)

        else:
            raise FileNotFoundError

    except FileNotFoundError:
        
        not_found_html = """<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>
<BODY>Not Found</BODY></HTML>"""
        c.send(b'HTTP/1.1 404 Not Found\r\n')
        c.send(b'\r\n')
        c.send(not_found_html.encode('euc-kr'))

    c.close()
