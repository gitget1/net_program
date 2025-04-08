import socket
import time

# 디바이스와 TCP 연결
dev1 = socket.socket()
dev2 = socket.socket()

dev1.connect(('127.0.0.1', 9001))
dev2.connect(('127.0.0.1', 9002))

def save_to_file(log):
    with open("data.txt", "a", encoding="utf-8") as f:
        f.write(log + "\n")

print("=== IoT 사용자 프로그램 ===")
print("1 = 디바이스1 요청, 2 = 디바이스2 요청, quit = 종료")

device1_count = 0
device2_count = 0

while True:
    command = input(">> ").strip().lower()
    now = time.ctime()

    if command == "1":
        dev1.send(b"request")
        data = dev1.recv(1024).decode()
        temp, humid, illum = data.split(",")
        log = f"{now}: Device1: Temp={temp}, Humid={humid}, Iilum={illum}"
        print(log)
        save_to_file(log)
        device1_count += 1

    elif command == "2":
        dev2.send(b"request")
        data = dev2.recv(1024).decode()
        hb, steps, cal = data.split(",")
        log = f"{now}: Device2: Heartbeat={hb}, Steps={steps}, Cal={cal}"
        print(log)
        save_to_file(log)
        device2_count += 1

    elif command == "quit":
        dev1.send(b"quit")
        dev2.send(b"quit")
        dev1.close()
        dev2.close()
        print("\n💾 프로그램 종료됨")
        print(f"총 수집 - Device1: {device1_count}개, Device2: {device2_count}개")
        break

    else:
        print("❗ 잘못된 명령입니다. '1', '2', 또는 'quit'을 입력하세요.")
