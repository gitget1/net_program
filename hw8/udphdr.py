
import struct
import binascii

# UDP 헤더 클래스 정의
class Udphdr:
    def __init__(self, src_port, dst_port, length, checksum):
        self.src_port = src_port
        self.dst_port = dst_port
        self.length = length
        self.checksum = checksum

    # UDP 헤더를 패킹하는 함수
    def pack_Udphdr(self):
        return struct.pack('!HHHH', self.src_port, self.dst_port, self.length, self.checksum)

# UDP 헤더 언패킹 함수
def unpack_Udphdr(buffer):
    return struct.unpack('!HHHH', buffer[:8])

# 필드별 getter 함수
def getSrcPort(unpacked_udpheader):
    return unpacked_udpheader[0]

def getDstPort(unpacked_udpheader):
    return unpacked_udpheader[1]

def getLength(unpacked_udpheader):
    return unpacked_udpheader[2]

def getChecksum(unpacked_udpheader):
    return unpacked_udpheader[3]

# 테스트
if __name__ == '__main__':
    # Udphdr 객체 생성
    udp = Udphdr(5555, 80, 1000, 0xFFFF)

    # 헤더 패킹
    packed_udp = udp.pack_Udphdr()
    print(binascii.b2a_hex(packed_udp))

    # 헤더 언패킹
    unpacked_udp = unpack_Udphdr(packed_udp)
    print(unpacked_udp)

    # 필드별 출력
    print("Source Port:{} Destination Port:{} Length:{} Checksum:{}".format(
        getSrcPort(unpacked_udp),
        getDstPort(unpacked_udp),
        getLength(unpacked_udp),
        getChecksum(unpacked_udp)
    ))
